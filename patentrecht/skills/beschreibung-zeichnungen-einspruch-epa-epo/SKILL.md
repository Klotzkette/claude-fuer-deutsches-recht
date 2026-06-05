---
name: beschreibung-zeichnungen-einspruch-epa-epo
description: "Beschreibung Zeichnungen Einspruch EPA EPO: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beschreibung Zeichnungen Einspruch EPA EPO

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beschreibung Zeichnungen Einspruch EPA EPO** im Plugin Patentrecht (Verfahren, Verletzung). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beschreibung-und-zeichnungen-pruefen` | Prüft Beschreibung, Zeichnungen, Bezugszeichenliste und Ausführungsbeispiele einer Patentanmeldung auf Offenbarungsstütze, Verständlichkeit, Anspruchskonsistenz, Varianten und formale Lücken. |
| `einspruch-epa-und-nichtigkeit-bpatg` | Bereitet EPA-Einspruch und deutsche Nichtigkeitsklage vor: Fristen, Zuständigkeit, Angriffsmittel, Stand der Technik, unzulässige Erweiterung, Ausführbarkeit, Priorität, Hilfsanträge und Prozessstrategie. |
| `epo-epue-einspruch-beschwerde-beschraenkung` | Vertieft EPA/EPO-Verfahren: Einspruch, Beschwerde, zentrale Beschränkung, Hilfsanträge, Verfahrenssprache, mündliche Verhandlung und Übergang zu UPC/nationaler Durchsetzung. |

## Arbeitsweg

Im Plugin Patentrecht (Verfahren, Verletzung) gilt für **Beschreibung Zeichnungen Einspruch EPA EPO**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beschreibung-und-zeichnungen-pruefen`

**Fokus:** Prüft Beschreibung, Zeichnungen, Bezugszeichenliste und Ausführungsbeispiele einer Patentanmeldung auf Offenbarungsstütze, Verständlichkeit, Anspruchskonsistenz, Varianten und formale Lücken.

# Beschreibung und Zeichnungen prüfen

## Prüfpunkte

1. **Technisches Gebiet:** knapp, ohne unnötige Einschränkung.
2. **Stand der Technik:** ehrlich, aber nicht selbstschädlich formulieren.
3. **Aufgabe:** technisch, nicht rein wirtschaftlich.
4. **Lösung:** Merkmale aus Anspruch 1 wiederfinden.
5. **Vorteile:** technische Wirkungen mit Bezug zu Merkmalen.
6. **Figuren:** jede Figur erklären; jedes Bezugszeichen konsistent verwenden.
7. **Ausführungsbeispiele:** nicht enger als nötig; Varianten und Äquivalente offenhalten.
8. **Stütze:** jedes Anspruchsmerkmal muss in der Beschreibung unmittelbar auffindbar sein.
9. **Keine späteren Überraschungen:** keine Merkmale nur in Zeichnungen verstecken, keine Widersprüche zwischen Anspruch und Beschreibung.

## Output

- Tabelle `Anspruchsmerkmal | Stütze in Beschreibung/Figur | Problem | Korrekturvorschlag`.
- Bezugszeichenliste.
- Liste fehlender Figuren oder technischer Angaben.
- Mandantenrückfragen.

## Typische Korrekturen

- unklare Begriffe definieren.
- mehrere Ausführungsformen getrennt beschreiben.
- Funktionsmerkmale durch Struktur- oder Prozessmerkmale absichern.
- technische Wirkung der Merkmale ausdrücklich verbinden.

## Pflicht-Normen und Risiken

- **§ 34 Abs. 4 PatG / Art. 83 EPÜ:** Erfindung muss so deutlich und vollständig offenbart sein, dass ein Fachmann sie ausführen kann. Bei mangelnder Offenbarung Zurückweisung / Nichtigkeit (§ 21 Abs. 1 Nr. 2 PatG, Art. 138 Abs. 1 b) EPÜ).
- **§ 38 PatG / Art. 123 (2) EPÜ Erweiterungsverbot:** Spätere Änderungen dürfen Offenbarung nicht über ursprüngliche Anmeldung hinaus erweitern. Achtung: Klassiker im Einspruch ("inadmissible amendment").
- **Stütze im Anspruch (§ 34 Abs. 3 Nr. 4 PatG / Art. 84 EPÜ):** Ansprüche müssen durch Beschreibung gestützt sein; jedes Anspruchsmerkmal in Beschreibung wiederzufinden.
- **Unzulässige Verallgemeinerung:** Aus Ausführungsbeispielen einzelne Merkmale herauspicken ("intermediate generalisation") ist riskant — Klage auf Nichtigkeit wahrscheinlich.
- **Klarheit Anspruch (Art. 84 EPÜ):** "Unmittelbar und eindeutig" entnehmbar; vage Begriffe wie "im Wesentlichen", "etwa" prüfen.
- **Zeichnungen:** Bezugszeichen konsistent mit Beschreibung; nur als Erläuterung, nicht zur Anspruchsbegrenzung.
- Tipp: Bei mehreren Ausführungsbeispielen Unteransprüche entsprechend gestaffelt anlegen — gibt im Einspruch/Nichtigkeitsverfahren Rückzugsposition.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `einspruch-epa-und-nichtigkeit-bpatg`

**Fokus:** Bereitet EPA-Einspruch und deutsche Nichtigkeitsklage vor: Fristen, Zuständigkeit, Angriffsmittel, Stand der Technik, unzulässige Erweiterung, Ausführbarkeit, Priorität, Hilfsanträge und Prozessstrategie.

# Einspruch und Nichtigkeit

## Weichenstellung

- **EPA-Einspruch:** nach Erteilung innerhalb der EPÜ-Frist; zentraler Angriff gegen europäisches Patent.
- **Nichtigkeitsklage:** deutscher Angriff gegen nationalen Teil, wenn zulässig und strategisch sinnvoll.
- **Parallelität:** Verletzungsverfahren, UPC, BPatG, EPA und Vergleichsverhandlungen koordinieren.

## Angriffsmittel

1. fehlende Neuheit.
2. fehlende erfinderische Tätigkeit.
3. nicht patentfähiger Gegenstand.
4. mangelnde Ausführbarkeit.
5. unzulässige Erweiterung.
6. unzulässige Erweiterung des Schutzbereichs nach Erteilung.
7. Prioritätsproblem.

## Beweispaket

| Angriff | Dokument/Beweis | Relevanz | Beweisqualität | Lücke |
| --- | --- | --- | --- | --- |

## Output

- Fristen- und Zuständigkeitsplan.
- Angriffsmittelmatrix.
- Entwurf Gliederung Einspruch/Nichtigkeitsklage.
- Hilfsantrags- und Beschränkungsprognose.
- Vergleichs- und Verletzungsprozessschnittstelle.

## Qualitätsregel

Offenkundige Vorbenutzung nur dann stark bewerten, wenn Zeit, Ort, Öffentlichkeit, konkrete technische Merkmale und Beweise sauber belegbar sind.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `epo-epue-einspruch-beschwerde-beschraenkung`

**Fokus:** Vertieft EPA/EPO-Verfahren: Einspruch, Beschwerde, zentrale Beschränkung, Hilfsanträge, Verfahrenssprache, mündliche Verhandlung und Übergang zu UPC/nationaler Durchsetzung.

# EPÜ: Einspruch, Beschwerde und Beschränkung

## Aufgabe

EPO-Post-Grant-Strategie zwischen Einspruch, Beschwerde, zentraler Beschränkung und nationaler/UPC-Durchsetzung.

## Einstieg

Frage zu Beginn nur die Punkte ab, die für die nächste irreversible Entscheidung gebraucht werden:

1. Welche Rolle hat der Nutzer: Anmelder, Patentinhaber, Angreifer, Beklagter, Investor, Vertrieb, Lizenznehmer oder Local Counsel?
2. Welche Schutzrechte, Produkte, Länder und Fristen sind betroffen?
3. Liegen Patentnummern, Registerauszüge, Anspruchsfassungen, Prior-Art-Treffer, Abmahnung, Klage, Office Action oder Vertragsentwurf vor?
4. Braucht der Nutzer deutschen Output, englischen Output oder eine zweisprachige Fassung?

## Arbeitsworkflow

1. **Frist und Beteiligtenstellung prüfen.**
2. **Grounds of opposition strukturiert erfassen.**
3. **Hilfsanträge nach Verteidigungsbreite ordnen.**
4. **Mündliche Verhandlung und technische Argumentationslinie vorbereiten.**
5. **Auswirkungen auf UPC/nationale Verfahren abgleichen.**


## Prüfmatrix

| Ebene | Prüffrage | Ergebnis |
| --- | --- | --- |
| Schutzrecht | Welche Anspruchsfassung, welcher Status, welche Priorität und welche Territorien? | Register live prüfen; Annahmen markieren. |
| Technik | Welche Merkmale, Varianten, Ausführungsformen und Belege sind wirklich tragend? | Merkmalsgliederung/Claim Chart. |
| Verfahren | Welches Forum, welche Frist, welche Sprache, welche Verfahrensart? | Forum- und Fristenampel. |
| Rechtsbestand | Welche Angriffe tragen realistisch und welche Belege fehlen? | Invalidity-/Opposition-Map. |
| Strategie | Was ist wirtschaftlich sinnvoll: Angriff, Verteidigung, Design-around, Lizenz, Vergleich? | Handlungsempfehlung. |

## Output

Erzeuge je nach Auftrag:

- Opposition/Appeal Roadmap.
- Auxiliary Request Tree.
- Oral Proceedings Script.
- Patent Family Impact Note.


## Anschluss-Skills

- `internationaler-patentrechts-und-laendercheck`, wenn weitere Länder oder Patentfamilien betroffen sind.
- `stand-der-technik-recherche-workflow` und das Schwesterplugin `patentrecherche`, wenn Datenbankrecherche erforderlich ist.
- `patentrecht-redteam-qualitygate`, bevor ein Ergebnis nach außen geht.

## Quellenregel

Keine erfundenen Registerstände, Fristen oder ausländischen Rechtsaussagen. Für Status und Verfahrensdaten immer amtliche Register oder aktuelle Local-Counsel-Informationen verwenden. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben; sonst als zu verifizieren markieren.
