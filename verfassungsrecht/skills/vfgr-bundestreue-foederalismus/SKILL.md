---
name: vfgr-bundestreue-foederalismus
description: "Vfgr Bundestreue Foederalismus: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vfgr Bundestreue Foederalismus

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vfgr Bundestreue Foederalismus** im Plugin Verfassungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vfgr-bundestreue-foederalismus-spezial` | Spezialfall Bundestreue und Foederalismus: ungeschriebener Verfassungsgrundsatz, Pflicht zur Ruecksicht. Pruefraster fuer Bund-Laender-Konflikte und Klagen Karlsruhe. |
| `vfgr-grundrechtspruefung-bauleiter` | Bauleiter Grundrechtspruefung: Schutzbereich, Eingriff, Rechtfertigung, Verhaeltnismaessigkeit. Pruefraster fuer Klausur und Schriftsatz. |
| `vfgr-organstreit-leitfaden` | Leitfaden Organstreit Art. 93 Abs. 1 Nr. 1 GG: Beteiligtenfaehigkeit, Antragsgegenstand, Antragsbefugnis. Pruefraster fuer Bundestagsfraktionen und Abgeordnete. |

## Arbeitsweg

Im Plugin Verfassungsrecht gilt für **Vfgr Bundestreue Foederalismus**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vfgr-bundestreue-foederalismus-spezial`

**Fokus:** Spezialfall Bundestreue und Foederalismus: ungeschriebener Verfassungsgrundsatz, Pflicht zur Ruecksicht. Pruefraster fuer Bund-Laender-Konflikte und Klagen Karlsruhe.

# VfgR: Bundestreue Foederalismus

## Fachkern: VfgR: Bundestreue Foederalismus
- **Spezialgegenstand:** VfgR: Bundestreue Foederalismus wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
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

## 2. `vfgr-grundrechtspruefung-bauleiter`

**Fokus:** Bauleiter Grundrechtspruefung: Schutzbereich, Eingriff, Rechtfertigung, Verhaeltnismaessigkeit. Pruefraster fuer Klausur und Schriftsatz.

# VfgR: Grundrechtspruefung

## Fachkern: VfgR: Grundrechtspruefung
- **Spezialgegenstand:** VfgR: Grundrechtspruefung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Bauleiter Grundrechtspruefung: Schutzbereich, Eingriff, Rechtfertigung, Verhaeltnismaessigkeit.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster — Drei-Schritt der Grundrechtspruefung

1. **Schutzbereich** — sachlich und persoenlich. Welches Grundrecht ist einschlaegig (Art. 1-19 GG)? Persoenlicher Schutzbereich (Deutsche/jedermann/juristische Personen Art. 19 III GG)? Sachlicher Schutzbereich nach BVerfG-Definition? Konkurrenzen pruefen (Spezialitaet, Idealkonkurrenz).
2. **Eingriff** — klassisch (final, unmittelbar, rechtsfoermig, mit Befehl und Zwang) oder modern (jede dem Staat zurechenbare nicht nur unwesentliche Beeintraechtigung). Schutzbereichsverkuerzung oder mittelbar-faktischer Eingriff?
3. **Verfassungsrechtliche Rechtfertigung**
 - Schranke: Vorbehalt des Gesetzes, einfacher/qualifizierter Gesetzesvorbehalt, verfassungsimmanente Schranken bei vorbehaltlosen Grundrechten (Art. 4, 5 III GG).
 - Schranken-Schranke: Verhaeltnismaessigkeit (legitimer Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit), Wesensgehalt Art. 19 II GG, Zitiergebot Art. 19 I 2 GG, Einzelfallverbot Art. 19 I 1 GG, Bestimmtheitsgebot.

## Praxisfallen

- Schutzbereich und Eingriff vermischen (Klassiker). Strenge Trennung im Schriftsatz.
- Bei Art. 12 I GG: Drei-Stufen-Theorie (Berufsausuebung/subjektive/objektive Zulassungsschranken).
- Bei Art. 14 I GG: Inhalts- und Schrankenbestimmung vs. Enteignung sauber abgrenzen (BVerfGE 58, 300 — Nassauskiesung).
- Bei Art. 3 I GG: Pruefungsmassstaeben (Willkuer vs. neue Formel) je nach Differenzierungsmerkmal.
- Bei Art. 2 I GG: Subsidiaritaet (nur wenn kein spezielleres Grundrecht greift).
- Drittwirkung: mittelbar ueber Generalklauseln (BVerfGE 7, 198 — Lueth).

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

## 3. `vfgr-organstreit-leitfaden`

**Fokus:** Leitfaden Organstreit Art. 93 Abs. 1 Nr. 1 GG: Beteiligtenfaehigkeit, Antragsgegenstand, Antragsbefugnis. Pruefraster fuer Bundestagsfraktionen und Abgeordnete.

# VfgR: Organstreit

## Fachkern: VfgR: Organstreit
- **Spezialgegenstand:** VfgR: Organstreit wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Leitfaden Organstreit nach Art. 93 I Nr. 1 GG, §§ 13 Nr. 5, 63 ff. BVerfGG. Pruefung von Beteiligtenfaehigkeit, Antragsgegenstand, Antragsbefugnis und Frist.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster Organstreit (Zulaessigkeit)

1. **Zustaendigkeit BVerfG** — Art. 93 I Nr. 1 GG, §§ 13 Nr. 5, 63 ff. BVerfGG.
2. **Parteifaehigkeit / Beteiligtenfaehigkeit** — § 63 BVerfGG: oberste Bundesorgane (Bundestag, Bundesrat, Bundespraesident, Bundesregierung) und andere durch GG oder Geschaeftsordnung mit eigenen Rechten ausgestattete Beteiligte (Fraktionen, einzelne Abgeordnete, Bundestagspraesident, Bundestagsausschuesse).
3. **Antragsgegenstand** — § 64 I BVerfGG: Massnahme oder Unterlassung des Antragsgegners.
4. **Antragsbefugnis** — § 64 I BVerfGG: Antragsteller muss eigene Rechte aus dem GG (oder organschaftliche Rechte) durch die beanstandete Massnahme/Unterlassung verletzt sein oder unmittelbar gefaehrdet sein koennen (Moeglichkeitstheorie).
5. **Form und Frist** — § 64 III BVerfGG: schriftlich, binnen sechs Monaten ab Bekanntwerden der beanstandeten Massnahme. Frist ist nicht verlaengerbar, keine Wiedereinsetzung in vorigen Stand (§ 93 II BVerfGG nur bei Verfassungsbeschwerde).
6. **Rechtsschutzbeduerfnis** — entfaellt z. B. bei Erledigung; Fortsetzungsfeststellungsantrag moeglich bei Wiederholungsgefahr oder Rehabilitierungsinteresse.

## Typische Konstellationen

- Abgeordnetenrechte (Art. 38 I 2 GG): Rede-, Frage-, Antrags-, Stimmrecht; Akteneinsicht; Untersuchungsausschuss-Mitwirkung.
- Fraktionsrechte aus GO-BT (Antragsrechte, Redezeitverteilung, Ausschussbesetzung).
- Informationsanspruch des Bundestages gegenueber Bundesregierung (Art. 38 I 2, 20 II 2 GG; BVerfGE 124, 78 — BND-Untersuchungsausschuss).
- Aeusserungsbefugnisse der Bundesregierung gegenueber politischen Parteien (BVerfGE 154, 320 — Seehofer/AfD).

## Abgrenzung

- **Bund-Laender-Streit (Art. 93 I Nr. 3 GG, §§ 68 ff. BVerfGG):** Streit ueber Rechte/Pflichten von Bund und Laendern, nicht von Bundesorganen untereinander.
- **Abstrakte Normenkontrolle (Art. 93 I Nr. 2 GG):** objektive Normpruefung, nicht subjektive Organrechtsverletzung.
- **Verfassungsbeschwerde (§ 90 BVerfGG):** Grundrechtstraeger gegen oeffentliche Gewalt, nicht Organe untereinander.

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
