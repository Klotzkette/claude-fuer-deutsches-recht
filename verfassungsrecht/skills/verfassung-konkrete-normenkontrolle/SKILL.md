---
name: verfassung-konkrete-normenkontrolle
description: "Verfassung Konkrete Normenkontrolle: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verfassung Konkrete Normenkontrolle

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verfassung Konkrete Normenkontrolle** im Plugin Verfassungsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verfassung-konkrete-normenkontrolle` | Konkrete Normenkontrolle Art. 100 Abs. 1 GG, §§ 80 ff. BVerfGG: Vorlage durch Gericht, das Gesetz fuer verfassungswidrig haelt. Vorlagepflicht und Entscheidungserheblichkeit. |
| `verfassung-parteiverbot` | Parteiverbot Art. 21 Abs. 2 GG, § 13 Nr. 2 BVerfGG: Voraussetzungen, NPD-Verfahren BVerfG 2 BvB 1/13. Pruefraster, hohe Schwelle (Potenzialitaet). Ausschluss von staatlicher Finanzierung Art. 21 Abs. 3 GG. |
| `verfassung-petition-und-verfassungsschutz` | Petitionsrecht Art. 17 GG und Verfassungsschutz: Verhaeltnis demokratische Teilhabe und Sicherheitsbehoerden. Beobachtung politischer Parteien und Akteure, Rechtsschutz vor VG. |

## Arbeitsweg

Im Plugin Verfassungsrecht gilt für **Verfassung Konkrete Normenkontrolle**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `verfassung-konkrete-normenkontrolle`

**Fokus:** Konkrete Normenkontrolle Art. 100 Abs. 1 GG, §§ 80 ff. BVerfGG: Vorlage durch Gericht, das Gesetz fuer verfassungswidrig haelt. Vorlagepflicht und Entscheidungserheblichkeit.

# Konkrete Normenkontrolle

## Fachkern: Konkrete Normenkontrolle
- **Spezialgegenstand:** Konkrete Normenkontrolle wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
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

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
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

## 2. `verfassung-parteiverbot`

**Fokus:** Parteiverbot Art. 21 Abs. 2 GG, § 13 Nr. 2 BVerfGG: Voraussetzungen, NPD-Verfahren BVerfG 2 BvB 1/13. Pruefraster, hohe Schwelle (Potenzialitaet). Ausschluss von staatlicher Finanzierung Art. 21 Abs. 3 GG.

# Parteiverbot

## Fachkern: Parteiverbot
- **Spezialgegenstand:** Parteiverbot wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Parteiverbot Art. 21 II GG iVm § 13 Nr. 2, §§ 43-47 BVerfGG; Finanzierungsausschluss Art. 21 III GG iVm § 13 Nr. 2a BVerfGG. Pruefraster, hohe Schwelle (Potentialitaet); Antragsbefugnis, Verfahren, Rechtsfolgen.


## Fachlicher Arbeitskern

Dieser Skill ist kein allgemeiner Chat-Modus, sondern ein Arbeitswerkzeug fuer `verfassungsrecht` zum Thema `verfassung-parteiverbot`. Ausgangspunkt ist immer die konkrete Aufgabe aus der Beschreibung: Parteiverbot Art. 21 Abs. 2 GG, § 13 Nr. 2 BVerfGG: Voraussetzungen, NPD-Verfahren BVerfG 2 BvB 1/13. Pruefraster, hohe Schwelle (Potenzialitaet). Ausschluss von staatlicher Finanzierung Art. 21 Abs. 3 GG..

Arbeite deshalb fallnah:

1. **Falltyp erkennen:** Einordnung, ob es um Erstberatung, Anspruchs-/Pflichtenpruefung, Vertrags-/Bescheid-/Schriftsatzarbeit, Strategie oder Fristenrettung geht.
2. **Entscheidungspunkte bilden:** Welche zwei bis fuenf Weichen entscheiden den Fall wirklich?
3. **Belege anfordern:** Nur die Unterlagen nachfordern, die fuer diese Weichen gebraucht werden; keine Frageboegen um ihrer selbst willen.
4. **Spezialwissen anwenden:** Die im Skill genannten Normen, Behoerden, Verfahrensarten, Branchenlogiken oder typischen Streitpunkte sichtbar abarbeiten.
5. **Nutzbaren Output liefern:** Am Ende steht ein Memo, eine Matrix, ein Textbaustein, ein Schriftsatzgeruest, ein Mandantenbrief oder eine klare Naechste-Schritte-Liste.

Wenn ein anderer Skill desselben Plugins genauer passt, schlage ihn aktiv vor und erklaere in einem Satz, warum der Wechsel die Arbeit beschleunigt.

## Einstieg
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster Parteiverbot Art. 21 II GG

### 1. Zulaessigkeit
- **Zustaendigkeit BVerfG** Art. 21 IV GG iVm § 13 Nr. 2, §§ 43 ff. BVerfGG.
- **Antragsberechtigte** § 43 I BVerfGG: Bundestag, Bundesrat, Bundesregierung. Nicht Landesregierungen (anders bei Vereinen § 3 VereinsG).
- **Antragsgegner**: die betroffene Partei (Art. 21 GG, § 2 PartG).
- **Form** § 23 BVerfGG: schriftlich mit Begruendung; Beweismittel.

### 2. Begruendetheit — materielle Voraussetzungen
- Partei muss
 - **nach ihren Zielen** (Programm, Satzung, Wahlprogramm) oder
 - **dem Verhalten ihrer Anhaenger** (organisierte Aktionen, nicht Einzelfaelle)
- darauf **ausgehen**, dass sie
 - die **freiheitliche demokratische Grundordnung beeintraechtigt oder beseitigt** oder
 - den **Bestand der BRD gefaehrdet**.

### 3. Potentialitaet (BVerfG, Urteil v. 17.01.2017, 2 BvB 1/13 — NPD II)
- "Darauf ausgehen" verlangt **aktives, planvolles Handeln** mit dem **Potenzial, das Ziel zu erreichen**.
- **Erfolgsmoeglichkeit** muss konkret bestehen; rein theoretisches Potenzial reicht nicht.
- Ist Partei chancenlos, fehlt Potentialitaet — kein Verbot moeglich; statt dessen evtl. Finanzierungsausschluss Art. 21 III GG.

### 4. Freiheitliche demokratische Grundordnung (BVerfGE 2, 1 — SRP; aktualisiert NPD II)
- Menschenwuerde Art. 1 GG.
- Demokratie- und Volkssouveraenitaetsprinzip.
- Rechtsstaatlichkeit.

### 5. Rechtsfolgen § 46 BVerfGG iVm § 33 PartG
- **Verbot** und **Aufloesung** der Partei.
- **Verbot Ersatzorganisation** § 33 II PartG.
- **Einziehung Vermoegen** zugunsten der oeffentlichen Hand.
- **Verlust Mandate** § 46 III BVerfGG (Abgeordnete verlieren Mandat).
- **Strafbarkeit** Fortfuehrung § 84 StGB.

### 6. Bindungswirkung § 31 BVerfGG
- BVerfG-Entscheidung bindet Bundes- und Landesverfassungsorgane, Gerichte, Behoerden.

## Pruefraster Finanzierungsausschluss Art. 21 III GG iVm § 46a BVerfGG

- Eingefuehrt 2017 nach NPD II als "Mildere-Variante" — kein Verbot, aber Ausschluss von staatlicher Finanzierung.
- Voraussetzungen: wie Verbot, aber **ohne Potentialitaet** (Erfolgsaussicht fehlt).
- Rechtsfolge: Ausschluss von staatlicher Parteienfinanzierung fuer **sechs Jahre** (§ 18 VII PartG); Wegfall Steuerbeguenstigung.
- BVerfG, Urteil v. 23.01.2024, 2 BvB 1/19 — "Die Heimat" (vormals NPD): erste erfolgreiche Anwendung Art. 21 III GG.

## Abgrenzung

- **Verfassungsschutz-Beobachtung** (§ 3 BVerfSchG): geringere Schwelle; Bundesamt fuer Verfassungsschutz.
- **Vereinsverbot** Art. 9 II GG, § 3 VereinsG: fuer Nicht-Parteien; durch BMI / Landesinnenministerien; Klage vor BVerwG (§ 4 VereinsG).
- **Parteienprivileg**: solange BVerfG nicht entschieden hat, geniesst Partei vollen Status (kein Vereinsverbot moeglich, keine Wahlteilnahme-Beschraenkung).

## Praxisfallen

- **V-Maenner-Problematik**: BVerfG, Beschluss v. 18.03.2003, 2 BvB 1/01 — NPD I (Einstellung). Nachrichtendienstliche Quellen muessen offengelegt sein; Abschaltverpflichtung.
- **Einstweilige Anordnung** § 32 BVerfGG bei Parteiverboten grds. ausgeschlossen.
- **Beweislast** beim Antragsteller; "in dubio pro reo" gilt entsprechend.
- **Anhaltspunkte aus Modellwissen** zu konkreten BVerfG-Az. immer live auf bundesverfassungsgericht.de verifizieren.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
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

## 3. `verfassung-petition-und-verfassungsschutz`

**Fokus:** Petitionsrecht Art. 17 GG und Verfassungsschutz: Verhaeltnis demokratische Teilhabe und Sicherheitsbehoerden. Beobachtung politischer Parteien und Akteure, Rechtsschutz vor VG.

# Petition + Verfassungsschutz

## Fachkern: Petition + Verfassungsschutz
- **Spezialgegenstand:** Petition + Verfassungsschutz wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
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

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
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
