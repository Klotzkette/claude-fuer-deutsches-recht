---
name: haus-plagiatscheck-themaeingrenzung
description: "Haus Plagiatscheck Themaeingrenzung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Haus Plagiatscheck Themaeingrenzung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Haus Plagiatscheck Themaeingrenzung** im Plugin Hausarbeitenmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `haus-plagiatscheck-eigenstaendigkeit-spezial` | Spezialfall Plagiatscheck und Eigenstaendigkeitserklaerung: Selbstplagiat, KI-Nutzung, Pruefungsrecht, Tools. Pruefraster fuer Pruefungsamt und Studierende. |
| `haus-themaeingrenzung-bauleiter` | Bauleiter Themaeingrenzung Hausarbeit: Forschungsfrage, Gliederungsentwurf, Literatursichtung. Pruefraster fuer Erstsemester und Examenskandidaten. |
| `meinungsstreit-darstellen` | Student muss Meinungsstreit in Hausarbeit darstellen: herrschende Meinung Mindermeinungen Argumente pro contra eigene Stellungnahme. Normen Methodenlehre wissenschaftliche Argumentation. Prüfraster Meinungs-Katalog Argument-Zuordnung Stellungnahme-Qualitaet Quellenbelege. Output strukturierter Meinungsstreit-Abschnitt eigene Argumentation. Abgrenzung zu metodenlehre-auslegung (Auslegungsmethoden) und quellenrecherche (Quellen finden). |

## Arbeitsweg

Im Plugin Hausarbeitenmacher gilt für **Haus Plagiatscheck Themaeingrenzung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `haus-plagiatscheck-eigenstaendigkeit-spezial`

**Fokus:** Spezialfall Plagiatscheck und Eigenstaendigkeitserklaerung: Selbstplagiat, KI-Nutzung, Pruefungsrecht, Tools. Pruefraster fuer Pruefungsamt und Studierende.

# Haus: Plagiatscheck Eigenstaendigkeit

## Spezialwissen: Haus: Plagiatscheck Eigenstaendigkeit
- **Spezialgegenstand:** Haus: Plagiatscheck Eigenstaendigkeit / haus plagiatscheck eigenstaendigkeit spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI.
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

## 2. `haus-themaeingrenzung-bauleiter`

**Fokus:** Bauleiter Themaeingrenzung Hausarbeit: Forschungsfrage, Gliederungsentwurf, Literatursichtung. Pruefraster fuer Erstsemester und Examenskandidaten.

# Haus: Themaeingrenzung

## Spezialwissen: Haus: Themaeingrenzung
- **Spezialgegenstand:** Haus: Themaeingrenzung / haus themaeingrenzung bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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

## 3. `meinungsstreit-darstellen`

**Fokus:** Student muss Meinungsstreit in Hausarbeit darstellen: herrschende Meinung Mindermeinungen Argumente pro contra eigene Stellungnahme. Normen Methodenlehre wissenschaftliche Argumentation. Prüfraster Meinungs-Katalog Argument-Zuordnung Stellungnahme-Qualitaet Quellenbelege. Output strukturierter Meinungsstreit-Abschnitt eigene Argumentation. Abgrenzung zu metodenlehre-auslegung (Auslegungsmethoden) und quellenrecherche (Quellen finden).

# Meinungsstreit darstellen

## Zweck

Der Meinungsstreit ist das Herzstück der Hausarbeit. Wer ihn nicht beherrscht, schreibt nur Routine. Wer ihn beherrscht, zeigt juristisches Denken.

## Schritt 1 — Wann ist ein Streit darzustellen?

### Voraussetzungen

- **Mindestens zwei rechtswissenschaftlich vertretbare Positionen** zum Tatbestandsmerkmal
- **Praktische Relevanz**: Das Ergebnis hängt von der Position ab
- **Belegbar**: Es gibt Vertreter mit Quellen-Nachweis

### Nicht jedem Detail einen Streit aufzwingen

Wenn der Streit nicht ergebnis-relevant ist (z.B. beide Meinungen kommen zum gleichen Ergebnis), genügt eine kurze Erwähnung.

## Schritt 2 — Standard-Struktur

```
1. Streit-Punkt (Frage / These)

2. Erste Position
 a) Auffassung
 b) Argumente / Begründung
 c) Quellen-Belege

3. Zweite Position (Mindermeinung / Gegen-Auffassung)
 a) Auffassung
 b) Argumente / Begründung
 c) Quellen-Belege

4. ggf. weitere Positionen

5. Stellungnahme
 a) Welche Argumente überzeugen mehr?
 b) Welche Position erscheint mit Begründung
 tragfähiger?
 c) Welches Ergebnis im konkreten Fall?
```

## Schritt 3 — Wendungen

### Streit-Eröffnung

- "Streitig ist, ob ..."
- "Hier stellt sich die Frage, ob ..."
- "In Rechtsprechung und Literatur wird diskutiert, ob ..."

### Position-Darstellung

- "Nach **herrschender Meinung** [Nachweis] ..."
- "Eine **Mindermeinung** [Nachweis] vertritt dagegen ..."
- "**Die Rechtsprechung** [Nachweis] sieht das ähnlich/anders, indem sie ..."
- "**In der Literatur** [Nachweis] wird ergänzend dargestellt, dass ..."

### Argumente einleiten

- "Für diese Auffassung spricht ..."
- "Argumentativ trägt diese Position ..."
- "Hierfür spricht der Wortlaut / die Systematik / die Genese / das Telos ..."

### Stellungnahme einleiten

- "Im Ergebnis überzeugt die herrschende Meinung, weil ..."
- "Die Argumente der Mindermeinung sind beachtlich, doch ..."
- "Für die hier vertretene Auffassung spricht entscheidend ..."

### Argumente abwägen

- "Die Mindermeinung hat den Vorzug, dass ... Allerdings ..."
- "Die herrschende Meinung kann sich auf ... berufen. Dem ist jedoch ..."

## Schritt 4 — Konkretes Beispiel — § 826 BGB-Sittenwidrigkeit

```
Streitig ist, ob das Verhalten des B als "sittenwidrig"
im Sinne des § 826 BGB einzustufen ist. Konkret stellt
sich die Frage, ob die wirtschaftliche Verfolgung
eigener Interessen, die für den Schädiger ungewöhnlich
hart ausfallen, als sittenwidrig zu qualifizieren ist.

**Nach herrschender Meinung** [Nachweis: vom Nutzer bereitgestellte oder lizenziert live geprüfte Quelle mit exakter Fundstelle;
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
auszulegen. Erforderlich ist ein besonders verwerfliches
Verhalten, das gegen das Anstandsgefühl aller billig
und gerecht Denkenden verstößt.

Argumente:
- Der Wortlaut "sittenwidrig" verlangt qualifizierten Unwert.
- Systematisch ist § 826 BGB als Auffang-Norm konzipiert,
 die nicht das Normalmaß rechtswidriger Schädigung erfasst.
- Telos: Schutz vor besonders verwerflicher Schädigung.

**Eine Mindermeinung** [Nachweis: Wagner, in:
lizenzpflichtige Literaturquelle BGB, 9. Aufl. 2025, § 826 BGB Rn. 17; Müller,
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Sittenwidrigkeit absenken und auch unverhältnismäßige
wirtschaftliche Schadens-Verfolgung erfassen.

Argumente:
- Der Schutz-Zweck des § 826 BGB könne nur
 durch erweiterte Auslegung erreicht werden.
- Die Praxis kennt zahlreiche Fall-Gruppen, in denen
 schon "kaufmännische" Härte als sittenwidrig
 bewertet wurde.

**Stellungnahme**:

Die wohl herrschende Meinung überzeugt im Ergebnis.
Der Wortlaut "sittenwidrig" verlangt qualifizierte
Verwerflichkeit. Eine Erweiterung würde § 826 BGB
zur generellen Korrektur deliktischer Konflikte machen
und damit den Charakter des § 823 II BGB / § 280 I BGB
Schutz-Systems überschreiten. Bei unverhältnismäßiger
Härte stehen vertrags-rechtliche Instrumente
(§ 313 BGB Anpassung) zur Verfügung.

Im konkreten Fall ist das Verhalten des B daher nicht
sittenwidrig. Es handelt sich um harte, aber rechtmäßige
Geschäftsführung. Folglich liegt kein § 826 BGB-Tatbestand
vor.
```

## Schritt 5 — Tiefe und Umfang

### Bei wesentlichen Streit-Punkten

- 1-2 Seiten Argumentation
- Mindestens 3-4 Quellen pro Position
- Eigene Stellungnahme deutlich

### Bei nebenstreitigen Punkten

- 1-3 Sätze
- Hinweis auf Streit, kurze Erwähnung
- Ergebnis ohne ausführliche Begründung

## Schritt 6 — Häufige Fehler

### Fehler 1: Streit ohne Praxis-Bezug

❌ "In der Literatur ist umstritten, ob ..."

✅ Streit mit konkretem Sachverhalt-Bezug subsumieren.

### Fehler 2: Nur eine Meinung darstellen

❌ Nur h.M. ohne Mindermeinung.

✅ Wenigstens **zwei** Positionen darstellen, auch wenn die h.M. überzeugt.

### Fehler 3: Keine eigene Stellungnahme

❌ "Die h.M. sagt X, die Mindermeinung sagt Y. Im Ergebnis ist X richtig."

✅ Begründete eigene Stellungnahme — warum X überzeugt.

### Fehler 4: Eigene Stellungnahme ohne Argument

❌ "Im Ergebnis überzeugt die Mindermeinung."

✅ "Im Ergebnis überzeugt die Mindermeinung, weil [Argument 1, Argument 2, Argument 3]."

### Fehler 5: Schwacher Beleg

❌ "Die h.M. sagt X (vgl. BGH)."

✅ Volle Fundstelle mit Randnummer.

### Fehler 6: Zu viele Streit-Punkte

❌ Bei jedem Tatbestandsmerkmal ein Streit-Punkt.

✅ Nur dort, wo ein Streit ergebnis-relevant ist.

## Schritt 7 — Stellungnahme-Strategie

### Sicher: Folge der h.M.

- Bei klar überlegener herrschender Meinung folge ihr
- Begründe trotzdem (nicht: "weil h.M.")

### Mutig: Folge der Mindermeinung

- Wenn die Mindermeinung überzeugendere Argumente hat
- Begründung muss besonders sorgfältig sein
- Riskanter, aber mit guten Argumenten möglich

### Eigene Auffassung entwickeln

- Bei erstmaligen oder neuartigen Konstellationen
- Mit besonderer Begründungs-Sorgfalt
- Nicht "erfinden", sondern auf bestehende Argumente zurückgreifen

## Schritt 8 — Tipps für die Praxis

### Hilfsfrage beim Lesen

- "Was sind die Schlüssel-Argumente jeder Position?"
- "Welche ist faktisch konsistenter?"
- "Welche ist juristisch konsistenter?"
- "Welche führt zu sachgerechteren Ergebnissen?"

### Methoden-Brücke

Die Argumente jeder Position lassen sich häufig auf die vier Auslegungs-Methoden (Wortlaut, Systematik, Historie, Telos) zurückführen. → Skill `methodenlehre-auslegung`

### Bei Streit zwischen Rechtsprechung und Literatur

- BGH-Linie ist praxis-relevant
- Literatur kann theoretisch besser begründet sein
- Häufig folgen Untergerichte der BGH-Linie

## Hilfsfragen für Deine Reflexion

- Habe ich den Streit **klar formuliert**?
- Habe ich **mindestens zwei Positionen** dargestellt?
- Habe ich für **jede Position Quellen**?
- Habe ich **Argumente** pro Position?
- Habe ich eine **begründete eigene Stellungnahme**?

## Übergang zu

- `methodenlehre-auslegung` — methodische Argumente
- `zitierweise-jura-fundstellen` — saubere Belege
- `selbstkontrolle-vor-abgabe` — Endcheck Streit-Stände
