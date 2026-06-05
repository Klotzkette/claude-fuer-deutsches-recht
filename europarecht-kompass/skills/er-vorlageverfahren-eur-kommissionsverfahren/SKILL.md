---
name: er-vorlageverfahren-eur-kommissionsverfahren
description: "ER Vorlageverfahren EUR Kommissionsverfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ER Vorlageverfahren EUR Kommissionsverfahren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **ER Vorlageverfahren EUR Kommissionsverfahren** im Plugin Europarecht (EuGH, EU-Kommission). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `er-kompass-spezial-vorlageverfahren` | Spezialfall Vorlageverfahren Art. 267 AEUV: Voraussetzungen, letztinstanzliche Vorlagepflicht, Cilfit-Kriterien, acte clair und acte eclaire, Folgen Verstoss (Staatshaftung Koebler). Pruefraster und Mustertext fuer Vorlagebeschluss. |
| `eur-kommissionsverfahren-art-258-spezial` | Spezialfall Vertragsverletzungsverfahren Art. 258 AEUV: Pilotphase, Mahnschreiben, mit Gruenden versehene Stellungnahme, Klage, Zwangsgeld Art. 260 AEUV. Pruefraster fuer Beschwerdefuehrer und Mitgliedstaat. Mustertexte. |
| `eur-mandant-uebersicht-zustaendigkeiten` | Mandantenuebersicht EU-Zustaendigkeiten: Kommission, Rat, Parlament, EuGH, EUG, EuRH, EZB. Pro Organ Aufgabe, Verfahrensbeteiligung, Klagewege. Routing-Tabelle fuer typische Mandantenanliegen. |

## Arbeitsweg

Im Plugin Europarecht (EuGH, EU-Kommission) gilt für **ER Vorlageverfahren EUR Kommissionsverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `er-kompass-spezial-vorlageverfahren`

**Fokus:** Spezialfall Vorlageverfahren Art. 267 AEUV: Voraussetzungen, letztinstanzliche Vorlagepflicht, Cilfit-Kriterien, acte clair und acte eclaire, Folgen Verstoss (Staatshaftung Koebler). Pruefraster und Mustertext fuer Vorlagebeschluss.

# Europarecht: Vorlageverfahren Art. 267

## Spezialwissen: Europarecht: Vorlageverfahren Art. 267
- **Spezialgegenstand:** Europarecht: Vorlageverfahren Art. 267 / er kompass vorlageverfahren. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 267, AEUV.
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

## 2. `eur-kommissionsverfahren-art-258-spezial`

**Fokus:** Spezialfall Vertragsverletzungsverfahren Art. 258 AEUV: Pilotphase, Mahnschreiben, mit Gruenden versehene Stellungnahme, Klage, Zwangsgeld Art. 260 AEUV. Pruefraster fuer Beschwerdefuehrer und Mitgliedstaat. Mustertexte.

# EU: Vertragsverletzung Art. 258

## Spezialwissen: EU: Vertragsverletzung Art. 258
- **Spezialgegenstand:** EU: Vertragsverletzung Art. 258 / eur kommissionsverfahren art 258 spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Art. 258, AEUV, Art. 260, EU.
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

## 3. `eur-mandant-uebersicht-zustaendigkeiten`

**Fokus:** Mandantenuebersicht EU-Zustaendigkeiten: Kommission, Rat, Parlament, EuGH, EUG, EuRH, EZB. Pro Organ Aufgabe, Verfahrensbeteiligung, Klagewege. Routing-Tabelle fuer typische Mandantenanliegen.

# EU: Zustaendigkeiten

## Aufgabe
Mandantenuebersicht EU-Zustaendigkeiten: Kommission, Rat, Parlament, EuGH, EUG, EuRH, EZB.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## EU-Organe und ihre Funktionen (Art. 13 EUV)

| Organ | Funktion | Verfahrensbeteiligung / Klagewege |
|---|---|---|
| **Europaeisches Parlament (EP)** | Mitgesetzgeber, Haushaltsbeschluss, Kontrolle Kommission | Petition Art. 24 II, 227 AEUV; Klagen Art. 263, 265 AEUV; PETI; Buergerbeauftragter Art. 228 AEUV |
| **Europaeischer Rat** | Politische Leitlinien, Vertragsaenderungen Art. 48 EUV | Keine Rechtsetzung im engeren Sinn; Klagen Art. 263 AEUV gegen Beschluesse moeglich |
| **Rat der Europaeischen Union** | Mitgesetzgeber, Koordinierung Wirtschaftspolitik | Mitwirkung am ordentlichen Gesetzgebungsverfahren Art. 294 AEUV |
| **Kommission** | Initiativrecht, Vollzug, Huetterin der Vertraege | Beschwerde wegen Vertragsverletzung Art. 258 AEUV; State Aid Art. 108 AEUV; Kartell Art. 105 AEUV |
| **EuGH (Court of Justice)** | Verfassungsgerichtsbarkeit der Union | Vorabentscheidung Art. 267 AEUV; Vertragsverletzung Art. 258, 259 AEUV; Rechtsmittel gegen EuG |
| **EuG (General Court)** | Erstinstanzgericht fuer Direktklagen | Nichtigkeitsklage Art. 263 AEUV; Untaetigkeit Art. 265 AEUV; Schadensersatz Art. 268, 340 AEUV (von Privaten) |
| **EuRH (Rechnungshof)** | Haushaltskontrolle | Keine streitigen Verfahren |
| **EZB** | Geldpolitik Eurozone, Aufsicht (SSM) | Klagen Art. 263 AEUV gegen EZB-Beschluesse |

## Routing fuer typische Mandantenanliegen

| Anliegen | Empfohlener Pfad |
|---|---|
| Auslegungsfrage Unionsrecht im laufenden nationalen Verfahren | Vorlageanregung an nationales Gericht (Art. 267 AEUV) |
| Mitgliedstaat verstoesst gegen Unionsrecht | Beschwerde an Kommission (Art. 258 AEUV); Petition EP (Art. 227 AEUV); SOLVIT |
| Akt der Union belastet Mandanten direkt | Nichtigkeitsklage Art. 263 IV AEUV (2-Monatsfrist), bei Verordnungen restriktiv (Plaumann) |
| Schaden durch Unionsorgane | Schadensersatzklage Art. 268, 340 II AEUV vor EuG |
| Beihilfe-Beschwerde | Notifikation Art. 108 III AEUV; Beschwerde nach VO 2015/1589 |
| Kartell/Marktmissbrauch | Kommission DG COMP; Schadensersatz nationale Gerichte (RL 2014/104/EU, §§ 33 ff. GWB) |
| Missstand EU-Verwaltung | Buergerbeauftragter Art. 228 AEUV |

## Pruefraster fuer den Skill

1. **Sachverhalt fixieren** — streitige und unstreitige Tatsachen, Lueckentafel.
2. **Unionsbezug pruefen** — Faellt die Materie in den Anwendungsbereich des Unionsrechts (Art. 51 GRC)?
3. **Zustaendiges Organ identifizieren** ueber die obige Tabelle.
4. **Rechtswegerschoepfung pruefen** (bei Untaetigkeitsklage Art. 265 AEUV: vorherige Aufforderung).
5. **Frist pruefen** (Art. 263 VI AEUV: zwei Monate ab Bekanntgabe oder Kenntnis).

## Praxisfallen

- **Plaumann-Formel** zur unmittelbaren und individuellen Betroffenheit Art. 263 IV AEUV ist sehr restriktiv; mit Lissabon erweitert auf "Rechtsakte mit Verordnungscharakter, die den Klaeger unmittelbar betreffen und keine Durchfuehrungsmassnahmen nach sich ziehen".
- Vorlagepflicht des letztinstanzlichen Gerichts Art. 267 III AEUV (CILFIT-Doktrin).
- Vertragsverletzungsverfahren Art. 258 AEUV: kein subjektiver Anspruch des Beschwerdefuehrers.

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
