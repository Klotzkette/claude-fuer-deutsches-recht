---
name: verl-aussagensicherheit-buchprojekt-bauleiter
description: "Verl Aussagensicherheit Buchprojekt Bauleiter: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verl Aussagensicherheit Buchprojekt Bauleiter

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Verl Aussagensicherheit Buchprojekt Bauleiter** im Plugin Verlagsredaktion. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verl-aussagensicherheit-pruefung` | Prueft im Manuskript jede tragende Aussage darauf ob sie so im Druck stehen darf: Belegtiefe Ehrenschutz Datenschutz Berufsrecht und Aussagewahrheit. |
| `verl-buchprojekt-bauleiter` | Bauleiter juristisches Buchprojekt: Konzept, Autorenvertrag, Manuskripteinreichung, Lektorat, Druck. Pruefraster fuer Herausgeber und Verlag. |
| `verl-email-konvolute-zu-fachbeitrag` | Verwertet einen E-Mail-Wechsel als Sachverhaltsquelle und Belegmaterial fuer eine Urteilsanmerkung oder einen Praxisbericht, mit Anonymisierung und Chronologie. |
| `verl-eskalation-bei-deadline-konflikt` | Eskalation bei Deadline-Konflikt: strukturierte Hochstufung von Manuskript-, Druck-, Honorar- oder Auslieferungsterminen mit Mustermails fuer Autor, Programmleitung und Geschaeftsfuehrung. |
| `verl-formatvorlage-check-autor-manuskript` | Prueft strikt die Einhaltung der Verlagsformatvorlage in Autorenmanuskripten und meldet Abweichungen so, dass der Autor sie selbst beheben kann. |

## Arbeitsweg

Im Plugin Verlagsredaktion gilt für **Verl Aussagensicherheit Buchprojekt Bauleiter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verl-aussagensicherheit-pruefung`

**Fokus:** Prueft im Manuskript jede tragende Aussage darauf ob sie so im Druck stehen darf: Belegtiefe Ehrenschutz Datenschutz Berufsrecht und Aussagewahrheit.

# Aussagensicherheits-Pruefung ("darf das so im Druck?")

## Worum geht es konkret

Eine Aussage in einem Fachaufsatz oder einer Anmerkung kann juristisch problematisch sein, selbst wenn Grammatik, Stil und Quellen stimmen: Sie kann ehrverletzend gegenueber Beteiligten sein, datenschutzrechtlich heikel, berufsrechtlich relevant (Mandantenidentifizierung!), oder einfach inhaltlich nicht hinreichend belegt. Dieser Skill ist das letzte inhaltliche Pruefraster vor Druck.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn immer bei brisanten Themen, polemischen Anmerkungen, Beitraegen mit erkennbarem Fall (Mandantenbezug), Beitraegen ueber konkret benannte Personen oder Institutionen. Klaeren Sie:

1. Werden konkrete Personen / Institutionen / Mandanten genannt?
2. Hat die Autorin ein Mandantenmandat selbst gefuehrt - dann § 43a BRAO?
3. Wird ein Berufsstand kritisiert (Richter, BMF, BAFin)?
4. Werden Rechtsmeinungen scharf abgelehnt - mit Belegen?

## Material- bzw. Sachrahmen

- Manuskript im finalen Stand.
- Hinweise auf Mandantenbezug.
- Vorgaengerbeitraege zum gleichen Thema (Konfliktlinien).
- Hauseigene Justiziariats-Richtlinien.

## Praxisleitfaden / Schritt fuer Schritt

1. **Risikoflaechen identifizieren:**
 - Mandantenbezug (Anwaltsmandat).
 - Konkret benannte Dritte (Richter, Anwaelte, Behoerden, Unternehmen).
 - Tatsachenbehauptungen (vs. Wertungen).
 - Anschuldigungen / Vorwuerfe.
 - Datenschutz-relevante Angaben.
2. **Belegtiefe pruefen.** Jede Tatsachenbehauptung mit Beleg? Wertungen als solche erkennbar?
3. **Ehrenschutz / Persoenlichkeitsrecht** (§§ 823, 1004 BGB, Art. 1 i.V.m. Art. 2 I GG): Werden Beteiligte ungerechtfertigt herabgesetzt?
4. **Mandantenschutz** (§ 43a Abs. 2 BRAO, § 203 StGB): Anonymisierung ausreichend? Schreibt die Autorin ueber einen eigenen Fall? Mandantenfreigabe?
5. **DSGVO** (Art. 6, Art. 9): personenbezogene Daten? Rechtsgrundlage?
6. **Berufsstandkritik.** Sachlich, mit Belegen? Oder polemisch ohne Grundlage?
7. **Wahrheits- / Wahrhaftigkeitsbeleg.** Tatsachenbehauptung muss erweislich wahr oder hinreichend recherchiert sein.
8. **Eskalation an Justiziariat** bei brisanten Stellen vor Druck.

## Trade-off-Matrix

| Pfad | A: Strenge Justiziariats-Vorpruefung | B: Verlagsroutine ohne Justiziariat | Empfehlung |
|------|--------------------------------------|--------------------------------------|------------|
| Risiko | gering | mittel bis hoch | A bei brisanten Themen |
| Lieferzeit | langsamer | schneller | B bei Routine |
| Beziehung Autor-Verlag | belastend | leichter | A wenn Risiko klar |

## Praxistipps der alten Redaktion

- "Schreibt die Autorin ueber einen eigenen Mandantenfall? Immer Mandantenfreigabe schriftlich, immer Anonymisierungspruefung."
- Personenkritik an Richtern: nur sachlich, nur mit Beleg, niemals ad personam.
- Anschuldigungen ("XY hat falsch entschieden") brauchen Belege, wo das Falsche liegt.
- Bei DSGVO-Themen: Datenschutzbeauftragte / Datenschutzbeauftragten des Verlages frueh einbinden.
- Im Zweifel an die Hausjustiziarin oder den externen Justiziar.

## Mustertexte / Vorlagen

**Risiko-Befundtabelle:**

| Stelle | Risikoart | Befund | Massnahme |
|--------|-----------|--------|-----------|
| S. 3 | Mandantenbezug | "Mein Mandant hatte ..." - Anonymisierung duenn | Mandantenfreigabe einholen, ggf. Anonymisierung verstaerken |
| S. 7 | Ehrenschutz Richter | "Der Vorsitzende hat erkennbar parteiisch verhandelt" - Behauptung ohne Beleg | Beleg verlangen oder Wertung zurueckziehen |
| S. 12 | DSGVO | Klarname eines Mandanten in Fussnote | streichen / anonymisieren |
| S. 18 | Berufsstandkritik | "Die BAFin hat versagt" - Beleg fehlt | konkretisieren mit Quelle |

**Anschreiben (Aussagensicherheit):**

> Sehr geehrte Frau Dr. Schmidt, bei der inhaltlichen Sicherheitspruefung Ihres Aufsatzes haben wir vier Stellen markiert, die wir vor Druck mit Ihnen besprechen wollen (siehe Anlage). Insbesondere bitten wir um (1) Mandantenfreigabe schriftlich fuer den Fallbezug S. 3, (2) Beleg fuer die Aussage zur Parteilichkeit S. 7, (3) Konkretisierung des Vorwurfs gegen die BAFin S. 18 mit Quelle. Die Stelle S. 12 (Mandantenname) bitten wir, vor Druck zu anonymisieren. Rueckmeldung bitte bis 19.06.2026.

**Eskalations-Notiz an Justiziariat:**

```
Manuskript: Schmidt, "[Titel]" fuer NJW 14/2026
Risikostufe: hoch
Risikoart: Personenkritik an Richter, Mandantenbezug
Anlagen: Manuskript, anonymisierte Beteiligten-Tabelle, vorgesehene Druckfassung
Bitte um Rueckmeldung bis 16.06.2026.
```

## Typische Fehler / Pitfalls

- Mandantenname uebersehen.
- Polemische Aussagen ohne Beleg im Druck.
- Justiziariat zu spaet eingebunden.
- DSGVO-Verletzung mit Klarnamen in Fussnoten.
- Rspr.-Kritik ad personam statt zur Sache.

## Querverweise

- `rechtecheck-urhg-verlg` - Urheber- und Verlagsrecht.
- `verl-relationslinien-pruefung-im-aufsatz` - Argumentationskritik.
- `verl-fussnoten-quellen-konsolidierung` - Beleg-Konsolidierung.
- `verl-stilbruch-stilcheck-fachzeitschrift` - Stilcheck.
- `ai-einsatz-transparenz-datenschutz` - Datenschutz beim KI-Einsatz.

## Quellen Stand 06/2026

- BGB §§ 823, 1004 (Ehrenschutz, Unterlassung), [https://www.gesetze-im-internet.de/bgb/](https://www.gesetze-im-internet.de/bgb/).
- StGB § 203 (Verletzung von Privatgeheimnissen), [https://www.gesetze-im-internet.de/stgb/](https://www.gesetze-im-internet.de/stgb/).
- BRAO § 43a Abs. 2 (Verschwiegenheit), [https://www.gesetze-im-internet.de/brao/](https://www.gesetze-im-internet.de/brao/).
- GG Art. 1 i.V.m. Art. 2 Abs. 1 (allg. Persoenlichkeitsrecht), [https://www.gesetze-im-internet.de/gg/](https://www.gesetze-im-internet.de/gg/).
- DSGVO Art. 6, Art. 9, [https://eur-lex.europa.eu/eli/reg/2016/679/oj](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
- KUG § 22 (Bildnisschutz).
- Pressekodex Ziff. 1, 2, 9, [https://www.presserat.de/pressekodex.html](https://www.presserat.de/pressekodex.html).

## 2. `verl-buchprojekt-bauleiter`

**Fokus:** Bauleiter juristisches Buchprojekt: Konzept, Autorenvertrag, Manuskripteinreichung, Lektorat, Druck. Pruefraster fuer Herausgeber und Verlag.

# Verl: Buchprojekt Bauleiter

## Spezialwissen: Verl: Buchprojekt Bauleiter
- **Spezialgegenstand:** Verl: Buchprojekt Bauleiter / verl buchprojekt bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGH, BVerfG.
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

## 3. `verl-email-konvolute-zu-fachbeitrag`

**Fokus:** Verwertet einen E-Mail-Wechsel als Sachverhaltsquelle und Belegmaterial fuer eine Urteilsanmerkung oder einen Praxisbericht, mit Anonymisierung und Chronologie.

# E-Mail-Konvolute zu Fachbeitrag

## Worum geht es konkret

Manchmal liefert eine Autorin den Sachverhalt eines geplanten Beitrags als E-Mail-Wechsel: Mandant - Anwalt - Behoerde - Gericht. Daraus wird ein Praxisbericht, eine Anmerkung zu einer Behoerdenpraxis oder eine Fallanalyse. Sie muessen den Wust anonymisieren, chronologisieren, zitierbar machen und entscheiden, was tatsaechlich in den Druck soll.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn, wenn E-Mails als Sachverhaltsbasis fuer einen Verlagsbeitrag dienen sollen. Klaeren Sie:

1. Liegt das Einverstaendnis aller Mailbeteiligten zur Verwertung vor?
2. Mandantenname, Aktenzeichen, Behoerdenname - was muss anonymisiert werden?
3. Welche Mails sind tatsaechlich relevant, welche sind Rauschen?
4. Zielformat (Praxisbericht, Anmerkung, Fallstudie)?

## Material- bzw. Sachrahmen

- .eml / .msg / .pst oder ausgedruckte Mails als PDF.
- Anlagen (Bescheide, Vertraege).
- Hinweise der Autorin zu Vertraulichkeit.
- Bei Anwaltsmandaten: Mandantenfreigabe schriftlich.

## Praxisleitfaden / Schritt fuer Schritt

1. **Vertraulichkeit klaeren.** Ohne schriftliche Freigabe der Mandantin oder anonymisierte Verwertung mit hinreichender Verfremdung: stop. § 43a Abs. 2 BRAO, § 203 StGB.
2. **Chronologie aufbauen.** Mails nach Sendedatum sortieren. Bei verschachtelten Threads: jede Mail als eigenes Element.
3. **Beteiligten-Tabelle.** Wer schreibt, wer empfaengt, welche Rolle? Pseudonymisieren (M = Mandantin, A = Anwalt, B = Behoerde, Az.-Code).
4. **Inhaltliche Verdichtung.** Mails sind oft 80 % Hoeflichkeitsfloskel - die 20 % Substanz extrahieren.
5. **Wortlautzitate sparsam.** Wo eine Behoerdenformulierung tragend ist, woertlich zitieren mit Anonymisierung der Beteiligten.
6. **Anlagen pruefen.** Bescheide, Vertraege - getrennt anonymisieren (Schwaerzungen sichtbar, nicht "weisse Flecken").
7. **Sachverhalt formulieren.** Aus dem Konvolut einen klassischen Tatsachenabsatz im Beitragsstil bauen. Mails werden zur Belegunterlage, nicht zum Druckinhalt.

## Trade-off-Matrix

| Pfad | A: Mails als Belegteil drucken | B: Nur Sachverhalt destillieren | Empfehlung |
|------|--------------------------------|--------------------------------|------------|
| Authentizitaet | hoch | mittel | A nur bei expliziter Freigabe und voller Anonymisierung |
| Lesbarkeit | gering (Brueche durch Formate) | hoch | B im Regelfall |
| Datenschutz / Berufsrecht | riskant | beherrschbar | B Standard |

## Praxistipps der alten Redaktion

- "Mailwechsel im Druck wirken selten gut. Lieber den Sachverhalt nacherzaehlen und nur eine zentrale Behoerdenpassage zitieren."
- Originalmails als Belegunterlage im Verlagsarchiv aufbewahren (Audit), aber nicht drucken.
- Anonymisierung: Personennamen, Adressen, Aktenzeichen, Bankverbindungen, Telefonnummern, IBAN, E-Mail-Adressen.
- Bei Mandantenmails: jede Verwendung im Beitrag braucht Mandantenfreigabe - die Anwaltin entscheidet das, nicht der Verlag.

## Mustertexte / Vorlagen

**Freigabe-Anschreiben an Autorin:**

> Sehr geehrter Herr Dr. Anwalt, fuer den Praxisbericht zur Behoerdenpraxis in Sachen [X] verwerten wir den uebersandten E-Mail-Wechsel als Sachverhaltsquelle. Wir benoetigen vor Druck: (1) die schriftliche Freigabe Ihrer Mandantin, (2) Bestaetigung der Anonymisierung (siehe Beleg-Anhang, anonymisierte Beteiligten-Tabelle), (3) Hinweis, ob die woertliche Wiedergabe der Behoerdenpassage vom 12.04.2026 im Druck erscheinen darf. Bitte bis 26.06.2026.

**Anonymisierungs-Schablone:**

```
M = Mandantin (privat, Mitte 50, NRW)
A = Anwalt (Verfasser des Beitrags)
B = Bauamt (Mittelstadt)
Az. = [Az. anonymisiert, 4-stellig: XXXX/24]
Datum = im Wortlaut erhalten
Ort = Stadt verfremdet ("Mittelstadt, NRW")
EUR = Betraege auf 1.000 EUR gerundet, wenn Identifikation droht
```

## Typische Fehler / Pitfalls

- Mandantenname stehen geblieben - Berufsrechtsverstoss.
- Bankverbindung / IBAN nicht entfernt.
- Anonymisierung so duenn, dass aus Kontext klar ist, wer gemeint ist.
- Mails als Originalformat (Schriftverkehr) ungeprueft in Layout uebernommen - Layout-Bruch.
- Chronologie verschoben durch Threading-Anzeigen aus Outlook.

## Querverweise

- `verl-roh-research-zu-essay` - aehnlicher Verwertungsprozess.
- `rechtecheck-urhg-verlg` - Rechte an fremden Mails.
- `quellen-zitate-fundstellencheck` - fuer Belegbehandlung.
- `verl-aussagensicherheit-pruefung` - "darf das so im Druck?".
- `workflow-dokumentenintake` - Intake.

## Quellen Stand 06/2026

- BRAO § 43a Abs. 2 (Verschwiegenheit), [https://www.gesetze-im-internet.de/brao/](https://www.gesetze-im-internet.de/brao/).
- StGB § 203, [https://www.gesetze-im-internet.de/stgb/](https://www.gesetze-im-internet.de/stgb/).
- DSGVO Art. 6, Art. 9.
- UrhG § 51 (Zitatschranke), § 63 (Quellenangabe).
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016.
- Moellers, Juristische Arbeitstechnik, 11. Aufl. 2023.

## 4. `verl-eskalation-bei-deadline-konflikt`

**Fokus:** Eskalation bei Deadline-Konflikt: strukturierte Hochstufung von Manuskript-, Druck-, Honorar- oder Auslieferungsterminen mit Mustermails fuer Autor, Programmleitung und Geschaeftsfuehrung.

# Eskalation bei Deadline-Konflikt

## Worum geht es konkret

Eine Frist droht zu reissen: Manuskripteingang verzoegert sich, Druckereitermin kollidiert mit Imprimatur, Autorenkorrektur kommt nicht zurueck, Vertriebstermin steht. Der Skill liefert ein eskalationsstufenfestes Vorgehen, das nicht zu frueh und nicht zu spaet zur Verlagsleitung greift, und Texte fuer jede Stufe.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welche Frist ist gefaehrdet (Abgabe, Imprimatur, Druck, Erscheinen)?
2. Wer haelt die Frist nicht ein (Autor, Lektorat, Herstellung, Vertrieb)?
3. Wieviel Puffer ist noch vorhanden (Tage, nicht Stunden)?
4. Was geschieht bei Fristversaeumnis (Haftung, Kosten, Imageschaden, Vertragsbruch)?
5. Welche Stufe ist bereits ausgereizt (Reminder, Mahnung, Telefonat, Termin)?
6. Wer hat Entscheidungsbefugnis fuer einen neuen Termin?

## Rechtlicher und sachlicher Rahmen

- VerlG §§ 30, 32 - Pflichten und Folgen bei Lieferverzug des Verfassers, Ruecktrittsrecht des Verlags bei wesentlicher Pflichtverletzung.
- BGB § 323 - Ruecktritt bei Nicht- oder Schlechtleistung; § 314 BGB Kuendigung aus wichtigem Grund bei Dauerverpflichtungen.
- BGB § 280 - Schadensersatz bei Pflichtverletzung; bei Verzug zusaetzlich §§ 286, 288 BGB.
- VerlG § 33 - Schadensersatz statt Leistung erst nach angemessener Nachfrist mit Ablehnungsandrohung.
- Druckereivertrag: AGB der Druckerei, oft mit Stornogebuehren bei Terminverschiebung.

## Praxisleitfaden / Schritt fuer Schritt

1. **Sachverhalt fixieren.** Wer hat wann was zugesagt, was ist eingegangen, was fehlt? In Schriftform dokumentieren.
2. **Stufe bestimmen.**
 - Stufe 1: Freundlicher Reminder mit Vorschlag zur Loesung.
 - Stufe 2: Erinnerung mit klarer neuer Frist, Hinweis auf Folgen.
 - Stufe 3: Mahnung mit Nachfristsetzung gemaess BGB § 323, Androhung des Ruecktritts.
 - Stufe 4: Eskalation an Programm- oder Verlagsleitung, ggf. an Justiziariat.
 - Stufe 5: Ruecktritt vom Vertrag, Schadensersatzgeltendmachung.
3. **Vor jeder Stufe pruefen:** Ist der vorherige Schritt schriftlich dokumentiert?
4. **Bei externer Beteiligung (Druckerei, Verteiler):** Parallel Plan B aktivieren, nicht erst nach Verstreichen der Frist.
5. **Nach Eskalation:** Stets schriftliche Bestaetigung des neuen Termins einholen.
6. **Lernschleife:** Nach Abschluss prueft die Redaktion, ob die Frist von Anfang an realistisch war.

## Trade-off-Matrix

| Aspekt | Frueh eskalieren | Spaet eskalieren |
|---|---|---|
| Beziehung zum Autor | Risiko der Beziehungsstoerung | Risiko des Frist-Reissens |
| Kosten | Vermeidung von Stornogebuehren | Mehr Aufwand bei Ad-hoc-Loesung |
| Image | Wirkt nervoes | Wirkt unzuverlaessig |
| Lerneffekt | Frueher Standard | Spaete Korrektur, oft zu spaet |

Empfehlung: lieber eine Stufe frueher als zu spaet.

## Praxistipps der alten Redaktion

- "Wer Stufe 1 ueberspringt, verliert die Bewegungsfreiheit." Immer freundlich anfangen.
- Bei wichtigen Autoren: Eskalation moeglichst durch Programmleitung, nicht durch Lektorat.
- Nie per E-Mail eskalieren, wenn ein Telefonat moeglich ist - aber jedes Telefonat schriftlich nachhalten.
- Imprimaturtermin haengt am Druckereitermin; Druckerei nie auf Verdacht stornieren.
- Bei wiederholten Versagen desselben Autors Hinweis in Personalakte / CRM, nicht nur im Lektoratsordner.

## Mustertexte / Vorlagen

**Stufe 1 - Freundlicher Reminder**

```
Betreff: Manuskript [Werktitel] - kurze Rueckfrage zum Stand

Sehr geehrte Frau/Herr [Autorenname],

ich melde mich kurz mit Blick auf den zugesagten Abgabetermin am [Datum].
Wie steht es um Ihren Manuskriptstand? Falls Sie ein wenig mehr Zeit
benoetigen, sprechen wir gerne ueber eine kleine Verschiebung; das Setzen
und der Druck sind aber an feste Termine gebunden.

Herzliche Gruesse
[Name]
```

**Stufe 3 - Mahnung mit Nachfristsetzung**

```
Betreff: Manuskript [Werktitel] - Mahnung und Nachfrist gemaess BGB § 323

Sehr geehrte Frau/Herr [Autorenname],

mit Verlagsvertrag vom [Datum] haben Sie sich verpflichtet, das Manuskript
zum [Datum] abzuliefern. Trotz unserer Erinnerungen vom [Datum] und
[Datum] ist das Manuskript bis heute nicht eingegangen.

Wir setzen Ihnen hiermit eine angemessene Nachfrist bis zum [Datum,
mindestens 14 Tage]. Sollte das Manuskript bis dahin nicht vollstaendig
vorliegen, werden wir vom Verlagsvertrag zuruecktreten und Schadensersatz
geltend machen (§§ 30, 32, 33 VerlG, § 323 BGB).

Wir wuerden ein konstruktives Gespraech ueber einen alternativen Termin
sehr begruessen.

Mit freundlichen Gruessen
[Name, Funktion]
```

**Stufe 4 - Eskalation an Verlagsleitung**

```
Betreff: Eskalation [Werktitel] - Entscheidungsbedarf bis [Datum]

[Empfaenger],

Sachstand: [3 Saetze]
Fristlage: [2 Saetze, mit Datum]
Bisher unternommene Schritte: [Aufzaehlung mit Daten]
Risiko bei Untaetigkeit: [konkret, Geld, Imprimatur, Vertrag]
Optionen:
A) [Loesung 1]
B) [Loesung 2]
C) Ruecktritt nach erfolgloser Nachfrist
Meine Empfehlung: [eine Option mit Begruendung]
Entscheidung bitte bis [Datum, Uhrzeit].
```

## Typische Fehler / Pitfalls

- Nachfristsetzung ohne klare Folgenandrohung - dann kein Ruecktrittsrecht.
- Eskalation per "Reply All" - Vertrauensbruch und falscher Verteiler.
- Druckerei zu spaet umbuchen - Stornogebuehren auf Verlagsseite.
- Mehrere Mahnungen ohne Eskalation - der Autor lernt, dass keine Konsequenz folgt.
- Mailverkehr nicht in CRM oder Lektoratsakte einpflegen - bei Rechtsstreit fehlt der Beweis.

## Querverweise

- `workflow-kaltstart-und-routing` - erste Einordnung des Konflikts.
- `workflow-fristen-und-risikoampel` - Ampelmethodik fuer Folgewirkungen.
- `verl-statusbericht-an-verlagsleitung` - Mantel fuer die Hochstufung.
- `verl-mahnung-an-autor-zahlung-frist` - bei Zahlungsverzug parallel zur Lieferung.
- `verl-abstimmung-mit-rechtsabteilung-pruefung` - vor Ruecktritt und Schadensersatzforderung.

## Quellen Stand 06/2026

- Gesetz ueber das Verlagsrecht (VerlG) vom 19.06.1901, zuletzt geaendert; insb. §§ 30, 32, 33 VerlG.
- BGB §§ 280, 286, 288, 314, 323 - Verzug, Ruecktritt, Kuendigung aus wichtigem Grund.
- BGB § 271 - Leistungszeit.
- Schricker/Loewenheim, Urheberrecht, aktuelle Auflage (vom Nutzer beizubringen) zu Verlagsverhaeltnissen.

## 5. `verl-formatvorlage-check-autor-manuskript`

**Fokus:** Prueft strikt die Einhaltung der Verlagsformatvorlage in Autorenmanuskripten und meldet Abweichungen so, dass der Autor sie selbst beheben kann.

# Formatvorlage-Check (Autor-Manuskript)

## Worum geht es konkret

Verlage haben Formatvorlagen (DOCX-Templates, LaTeX-Klassen, Schreibrichtlinien). Autorinnen halten sich selten daran. Der Format-Check ist die erste Pruefung nach Manuskripteingang: Stimmen Absatzformate, Ueberschriftenhierarchie, Fussnotenstil, Zitiernormen mit der Verlagsvorlage ueberein? Sie zeigen die Abweichungen, statt sie still zu korrigieren - sonst verlernt die Autorin nie.

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen ihn unmittelbar nach Eingang eines Manuskripts. Klaeren Sie:

1. Welches Verlagsformat (NJW-Manuskriptrichtlinien, JuS-Vorlage, hauseigener LaTeX-Stil)?
2. Hat die Autorin die Richtlinien bekommen (mit Datum)?
3. Welche Toleranzen (welche Abweichungen sind harmlos, welche stoppen die Annahme)?
4. Wie viel Eingriff vom Lektorat erwuenscht (still korrigieren oder zurueckspielen)?

## Material- bzw. Sachrahmen

- Verlagsformatvorlage (.dotx, Style Guide, LaTeX-Class).
- Autorenmanuskript.
- Eingangsmail mit Hinweis auf Manuskriptrichtlinien.

## Praxisleitfaden / Schritt fuer Schritt

1. **Eingangs-Sicherung.** Manuskript-Original ablegen, Arbeitskopie anlegen mit Versions-Stempel.
2. **Strukturpruefung.** Ueberschriftenhierarchie (Verlagsvorlage: H1, H2, H3?), maximale Verschachtelungstiefe.
3. **Absatzformate.** Standardabsatz, Zitatabsatz, Aufzaehlung, Fussnotentext - mit Verlagsformatvorlage abgeglichen?
4. **Fussnoten.** Position (Seitenfuss vs. Kapitelende), Zitiernorm (siehe `verl-zitierweise-pruefung-zeitschrift-jus-njw`), Nummerierung.
5. **Sonderzeichen.** § mit U+00A0 davor (geschuetzt), Anfuehrungszeichen, Bindestrich vs. Gedankenstrich.
6. **Bilder, Tabellen, Schaubilder.** Format, Verankerung, Beschriftung, Quellen.
7. **Inhaltsverzeichnis und Verweise.** Werden Querverweise automatisch generiert? Funktioniert das ToC?
8. **Befund-Tabelle.** Spalten: Element, Verlagsvorgabe, Befund, Stop/OK, Anmerkung. An Autorin zurueckspielen.

## Trade-off-Matrix

| Pfad | A: Stille Lektoratskorrektur | B: Manuskript zurueck an Autorin | Empfehlung |
|------|------------------------------|----------------------------------|------------|
| Verlagsaufwand | hoch | mittel | A nur bei nahem Druck und kooperativer Autorin |
| Lerneffekt Autorin | null | hoch | B im Regelfall |
| Lieferzeit | schnell | langsamer | A bei Zeitnot |
| Standardfall | B mit fristgebundenem "Nachbessern bis ..." |

## Praxistipps der alten Redaktion

- "Eine Autorin, die ihre Formatfehler nicht selbst korrigiert, wird sie beim naechsten Beitrag wiederholen. Lieber einmal genau zurueckspielen."
- Nicht jeden Mini-Fehler zurueckweisen - eine Befund-Tabelle mit 50 Punkten frustriert. Top-5-Stops, der Rest als "wuenschenswert".
- Bei wiederkehrenden Autorinnen einen "Hauseigenen Stilkatalog" pflegen - das spart Arbeit.
- LaTeX-Manuskripte schauen oft "richtig" aus, haben aber Klassenkonflikte. Probekompilation immer.

## Mustertexte / Vorlagen

**Rueckmeldung an Autorin (Format-Defekt):**

> Sehr geehrter Herr Dr. Schmidt, vielen Dank fuer Ihr Manuskript zu "[Titel]" vom 02.06.2026. Bei der Eingangspruefung haben wir die Einhaltung der NJW-Manuskriptrichtlinien geprueft (siehe NJW-Hinweise Stand 04/2026, in der Anlage). Sieben Stops haben wir markiert (siehe Befundtabelle, Anlage). Bitte ueberarbeiten Sie das Manuskript bis 16.06.2026. Bei Rueckfragen erreichen Sie uns unter ...

**Befund-Tabelle (Vorlage):**

| # | Element | Verlagsvorgabe | Befund | Stop/OK |
|---|---------|-----------------|--------|---------|
| 1 | Ueberschriftenhierarchie | max. 3 Ebenen | 5 Ebenen verwendet | Stop |
| 2 | Fussnoten-Position | Seitenfuss | Kapitelende | Stop |
| 3 | Zitierweise BGH | "Datum, Az, NJW Jahr, Seite (Rn)" | "Datum, NJW Jahr, S." (ohne Az.) | Stop |
| 4 | Anfuehrungszeichen | deutsch ("..." mit unten/oben) | englisch ("...") | wuenschenswert |

**Stilkatalog-Auszug (Beispiel NJW):**

```
- Paragraphenzeichen § stets mit geschuetztem Leerzeichen davor.
- Aktenzeichen mit Schraegstrich, ohne Bindestriche: "I ZR 12/24".
- Randnummer "Rn.", nicht "RN" oder "Tz." (Tz. nur bei BFH).
- "Bundesgerichtshof" bei Erstnennung, danach "BGH".
- Datum: "12.05.2026" (DD.MM.YYYY).
```

## Typische Fehler / Pitfalls

- Befund-Tabelle ohne Prioritaeten - Autorin liest 50 Punkte und uebersieht die 5 wichtigen.
- Stille Korrektur ohne Hinweis - Autorin lernt nicht.
- Manuskriptrichtlinien nicht verlinkt - Autorin weiss nicht, wonach sie pruefen soll.
- LaTeX-Manuskript ohne Probekompilation freigegeben.
- Zitiernorm-Check vergessen - landet erst in der Fahnenpruefung als Drama.

## Querverweise

- `verl-manuskript-merkwuerdige-formate-rettung` - bei Formatchaos.
- `verl-zitierweise-pruefung-zeitschrift-jus-njw` - Zitiernorm separat.
- `verl-fussnoten-quellen-konsolidierung` - Fussnotenpflege.
- `verl-redaktionelle-rueckmeldung-formulieren` - Stil der Rueckmeldung.
- `workflow-dokumentenintake` - Intake-Workflow.

## Quellen Stand 06/2026

- NJW-Manuskriptrichtlinien (vom Verlag bezogen, Stand jeweils im Manuskriptbearbeitungspaket).
- Duden, Die deutsche Rechtschreibung, 29. Aufl. 2024.
- Byrd / Lehmann, Zitierfibel fuer Juristen, 2. Aufl. 2016.
- Moellers, Juristische Arbeitstechnik, 11. Aufl. 2023.
- Schimmel, Juristische Klausuren und Hausarbeiten richtig formulieren, 13. Aufl. 2022.
