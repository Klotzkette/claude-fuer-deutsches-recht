---
name: famr-mandantenaufnahme-regenbogenfamilien
description: "Famr Mandantenaufnahme Regenbogenfamilien: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Famr Mandantenaufnahme Regenbogenfamilien

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Famr Mandantenaufnahme Regenbogenfamilien** im Plugin Fachanwalt Familienrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `famr-mandantenaufnahme-spezial` | Mandantenaufnahme im Familienrecht: emotionale Lage, Eilbedarf (Gewaltschutz, Kindeswohlgefaehrdung, Wegnahme Kind), Vertraulichkeit Familienangehoerige, Verfahrenskostenhilfe. Strukturiertes Erstgespraechs-Protokoll und Mustertext Mandatsbestaetigung. |
| `famr-regenbogenfamilien-recht-spezial` | Spezialfall Regenbogenfamilien: rechtliche Elternschaft nach BGH, Stiefkindadoption, Co-Mutter-Anerkennung, Reform des Abstammungsrechts (Entwurf 2024 ff.), Sorgerecht bei Trennung. Pruefraster und aktueller Rechtsprechungsstand. |
| `famr-versorgungsausgleich-spezial` | Spezialfall Versorgungsausgleich: VersAusglG, Anrechte Berechnung pro Versorgungstraeger, externe Teilung, interne Teilung, Anpassung wegen Unterhaltszahlung. Pruefraster und Beispielsfall. Schnittstelle Rentenversicherung. |
| `fehlerhafte-auskunft-versorgungstraeger` | Fehlerhafte Auskunft Versorgungsträger: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte. |
| `fragebogen-versorgungsausgleich-ausfuellen` | zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Fragebogen Versorgungsausgleich ausfüllen. |

## Arbeitsweg

Im Plugin Fachanwalt Familienrecht gilt für **Famr Mandantenaufnahme Regenbogenfamilien**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `famr-mandantenaufnahme-spezial`

**Fokus:** Mandantenaufnahme im Familienrecht: emotionale Lage, Eilbedarf (Gewaltschutz, Kindeswohlgefaehrdung, Wegnahme Kind), Vertraulichkeit Familienangehoerige, Verfahrenskostenhilfe. Strukturiertes Erstgespraechs-Protokoll und Mustertext Mandatsbestaetigung.

# Familienrecht: Mandantenaufnahme

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Familienrecht: Mandantenaufnahme` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Familienrecht: Mandantenaufnahme
- **Spezialgegenstand:** Familienrecht: Mandantenaufnahme / famr mandantenaufnahme spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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

## 2. `famr-regenbogenfamilien-recht-spezial`

**Fokus:** Spezialfall Regenbogenfamilien: rechtliche Elternschaft nach BGH, Stiefkindadoption, Co-Mutter-Anerkennung, Reform des Abstammungsrechts (Entwurf 2024 ff.), Sorgerecht bei Trennung. Pruefraster und aktueller Rechtsprechungsstand.

# Familienrecht: Regenbogenfamilien

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Familienrecht: Regenbogenfamilien` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Familienrecht: Regenbogenfamilien
- **Spezialgegenstand:** Familienrecht: Regenbogenfamilien / famr regenbogenfamilien recht spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGH.
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

## 3. `famr-versorgungsausgleich-spezial`

**Fokus:** Spezialfall Versorgungsausgleich: VersAusglG, Anrechte Berechnung pro Versorgungstraeger, externe Teilung, interne Teilung, Anpassung wegen Unterhaltszahlung. Pruefraster und Beispielsfall. Schnittstelle Rentenversicherung.

# FamR: Versorgungsausgleich

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `FamR: Versorgungsausgleich` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: FamR: Versorgungsausgleich
- **Spezialgegenstand:** FamR: Versorgungsausgleich / famr versorgungsausgleich spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** VersAusglG.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 4. `fehlerhafte-auskunft-versorgungstraeger`

**Fokus:** Fehlerhafte Auskunft Versorgungsträger: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: VersAusglG, FamFG Scheidungsverbund und Beschwerde, SGB VI, Beamtenversorgung, BetrAVG, Versorgungsträgerauskünfte.

# Fehlerhafte Auskunft Versorgungsträger

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fehlerhafte Auskunft Versorgungsträger` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Fehlerhafte Auskunft Versorgungsträger
- **Spezialgegenstand:** Fehlerhafte Auskunft Versorgungsträger. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Fehlerhafte Auskunft Versorgungsträger** im Bereich **Fachanwalt Familienrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Familienrecht mit besonderer Vertiefung Versorgungsausgleich, Scheidung, Unterhalt, Zugewinn, Kindschaftssachen und FamFG-Verfahren.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 5. `fragebogen-versorgungsausgleich-ausfuellen`

**Fokus:** zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Fragebogen Versorgungsausgleich ausfüllen.

# Fragebogen Versorgungsausgleich ausfüllen

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fragebogen Versorgungsausgleich ausfüllen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Fachkern: Fragebogen Versorgungsausgleich ausfüllen
- **Spezialgegenstand:** Fragebogen Versorgungsausgleich ausfüllen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Fragebogen Versorgungsausgleich ausfüllen** im Bereich **Fachanwalt Familienrecht**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Familienrecht mit besonderer Vertiefung Versorgungsausgleich, Scheidung, Unterhalt, Zugewinn, Kindschaftssachen und FamFG-Verfahren.

## Startfragen
- Was soll sofort entstehen: Kurztriage, Aktenplan, Fragenliste, Memo, Schriftsatz, Vertrag, Formular oder Mandantenbrief?
- Wo drohen Fristen, Formerfordernisse, Bußgelder, Gebührennachteile, Verfahrensfehler oder irreversible Schritte?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?
