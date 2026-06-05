---
name: tbm-grundrechte-grch-kandidatenloesung
description: "TBM Grundrechte Grch Kandidatenloesung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# TBM Grundrechte Grch Kandidatenloesung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **TBM Grundrechte Grch Kandidatenloesung** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gegen-tbm-und-einreden-pruefen` | Prüft rechtshindernde, rechtsvernichtende und rechtshemmende Einwendungen und Einreden: Nichtigkeitsgründe, Anfechtung, Erfuellung, Aufrechnung, Verjährung, Zurückbehaltungsrecht, Verwirkung, Verzicht. Strukturierte Gegenprüfung nach Anspruchsaufbau. |
| `grundrechte-pruefung-de-und-grch` | Prüft Grundrechte nach GG (Drei-Schritt: Schutzbereich, Eingriff, Rechtfertigung) und GRCh (Art. 51/52 GRCh). Unterscheidet Abwehr-, Leistungs- und Schutzpflichtdimension. Verhältnismäßigkeitsprüfung mit Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit. |
| `kandidatenloesung-subsumtion-pruefen` | Prueft abgegebene Klausur- oder Probandenloesungen auf Obersatz, Definition, Untersatz, Beleg, Ergebnis und typische Scheinkausalitaet. Gibt Korrekturvermerk mit Punkteindikation und Musterpassage. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **TBM Grundrechte Grch Kandidatenloesung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gegen-tbm-und-einreden-pruefen`

**Fokus:** Prüft rechtshindernde, rechtsvernichtende und rechtshemmende Einwendungen und Einreden: Nichtigkeitsgründe, Anfechtung, Erfuellung, Aufrechnung, Verjährung, Zurückbehaltungsrecht, Verwirkung, Verzicht. Strukturierte Gegenprüfung nach Anspruchsaufbau.

# Gegen-TBM und Einreden prüfen

## Triage zu Beginn — kläre vor der Gegenprüfung

1. Ist der Anspruch dem Grunde nach bereits positiv subsumiert?
2. Welche Einwendungen hat der Anspruchsgegner erhoben oder könnte er erheben?
3. Besteht eine Aufrechnungslage (§§ 387 ff. BGB)? — fällig, gleichartig, gegenseitig?
4. Ist Verjährung eingreifend? → Skill `verjaehrung-fristen-pruefen` parallel nutzen
5. Hat der Gläubiger durch sein Verhalten einen Vertrauenstatbestand gesetzt? → Verwirkung prüfen

## Zweck

Nach der positiven Subsumtion (Anspruch entstanden dem Grunde nach) prüft dieser Skill, ob Einwendungen oder Einreden des Anspruchsgegners den Anspruch ausschließen, vernichten oder hemmen. Dieser Schritt ist zwingend, bevor ein Ergebnis ausgegeben wird.

## Zentrale Paragrafenkette

- §§ 104-113 BGB — Geschäftsfähigkeit (rechtshindernde Einwendung bei Mangel)
- § 125 BGB — Nichtigkeit wegen Formmangels
- §§ 119, 120, 123 i.V.m. § 142 Abs. 1 BGB — Anfechtung (ex tunc-Nichtigkeit)
- §§ 305-310 BGB — AGB-Recht, Einbeziehung und Inhaltskontrolle
- § 362 BGB — Erfüllung als rechtsvernichtende Einwendung
- §§ 387-396 BGB — Aufrechnung (Aufrechnungslage, Aufrechnungserklärung)
- § 397 BGB — Erlass (vertraglicher Forderungsverzicht)
- §§ 194-217 BGB — Verjährung (Einrede, nicht Einwendung — § 214 BGB)
- § 273 BGB, § 320 BGB — Zurückbehaltungsrecht, Einrede des nicht erfüllten Vertrags
- § 242 BGB — Verwirkung (Treu und Glauben)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Systematik der Gegenrechte

### 1. Rechtshindernde Einwendungen (Anspruch entsteht gar nicht)

Rechtshindernde Einwendungen verhindern die Entstehung des Anspruchs:
- **Geschäftsunfähigkeit** (§ 104 BGB): Rechtsgeschäft nichtig; Anspruch nie entstanden
- **Formmangel** (§ 125 BGB): Nichtigkeit bei Nichteinhaltung der gesetzlichen Form
- **Sittenwidrigkeit / Gesetzesverstoß** (§§ 134/138 BGB): Nichtigkeit
- **Anfechtung** (§§ 119/120/123 BGB i.V.m. § 142 Abs. 1 BGB): Nichtigkeit ex tunc (rückwirkend)
- **AGB-Unwirksamkeit** (§§ 305 ff. BGB): Klausel nicht wirksam einbezogen oder inhaltlich unwirksam
- **Unmöglichkeit bei Vertragsschluss** (§ 311a BGB): Primärleistungspflicht entfällt

### 2. Rechtsvernichtende Einwendungen (Anspruch ist erloschen)

- **Erfüllung** (§ 362 BGB): Leistung bewirkt; Anspruch erloschen
- **Aufrechnung** (§§ 387 ff. BGB): Gegenforderung des Schuldners; Fälligkeit, Gleichartigkeit, Aufrechnungslage
- **Erlass** (§ 397 BGB): Vertraglicher Verzicht auf Forderung
- **Rücktritt** (§§ 346 ff. BGB): Rückabwicklung; Rücktrittsrecht muss vorliegen
- **Widerruf** (§§ 355 ff. BGB): Verbraucherverträge; Widerrufsfrist 14 Tage; beginnt mit ordnungsgemäßer Belehrung

### 3. Rechtshemmende Einreden (Anspruch besteht, ist aber nicht durchsetzbar)

- **Verjährung** (§§ 194 ff. BGB): Einrede, nicht Einwendung; muss erhoben werden (§ 214 BGB). Regelfall: 3 Jahre, Kenntnis ab Jahresende. Details in Skill `verjaehrung-fristen-pruefen`.
- **Zurückbehaltungsrecht** (§ 273 BGB / § 320 BGB): Leistung Zug-um-Zug; Fälligkeit der Gegenforderung
- **Einrede des nicht erfüllten Vertrags** (§ 320 BGB): Vorleistungspflicht beachten
- **Stundung**: Fälligkeit noch nicht eingetreten

### 4. Verwirkung (§ 242 BGB)

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 5. Mitverschulden (§ 254 BGB)

Kein vollständiger Ausschluss, aber Kürzung des Anspruchs. Das System fragt: Hat der Anspruchsteller selbst zum Schaden beigetragen? Welcher Anteil?

## Entscheidungsbaum Gegenprüfung

```
Ist ein Nichtigkeitsgrund vorhanden?
├─ Ja → rechtshindernde Einwendung → Anspruch nicht entstanden
└─ Nein → Ist ein Erlöschensgrund vorhanden?
 ├─ Ja → rechtsvernichtende Einwendung → Anspruch erloschen
 └─ Nein → Liegt eine Einrede vor (Verjährung, ZBR, § 320)?
 ├─ Ja (und erhoben) → Anspruch nicht durchsetzbar
 └─ Nein → Mitverschulden § 254 BGB prüfen → Quote
```

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Tabelle aller geprüften Gegenrechte mit Ergebnis (eingreifend / nicht eingreifend / fraglich). Gesamtergebnis: Anspruch besteht vollständig / gemindert / nicht durchsetzbar / nicht entstanden.

**Adressat:** Richter/Anwalt — Tonfall sachlich-juristisch

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

<!-- AUDIT 27.05.2026
-->

## 2. `grundrechte-pruefung-de-und-grch`

**Fokus:** Prüft Grundrechte nach GG (Drei-Schritt: Schutzbereich, Eingriff, Rechtfertigung) und GRCh (Art. 51/52 GRCh). Unterscheidet Abwehr-, Leistungs- und Schutzpflichtdimension. Verhältnismäßigkeitsprüfung mit Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit.

# Grundrechte prüfen — GG und GRCh

## Zweck

Dieser Skill führt die klassische Grundrechtsprüfung nach dem Grundgesetz und der Grundrechtecharta durch. Er unterscheidet die Schutzrichtungen der Grundrechte, klärt den Anwendungsbereich der GRCh und führt die Verhältnismäßigkeitsprüfung strukturiert durch.

## Drei-Schritt-Schema der Grundrechtsprüfung

### Schritt 1 — Schutzbereich

**Sachlicher Schutzbereich:** Welches Verhalten, welche Rechtspositionen schützt das Grundrecht?

- Art. 5 Abs. 1 GG: Meinungsfreiheit — Werturteile; keine Tatsachenbehauptungen (str.); keine Schmähkritik
- Art. 12 Abs. 1 GG: Berufsfreiheit — Wahl und Ausübung von Beruf und Arbeit
- Art. 14 Abs. 1 GG: Eigentum — vermögenswerte Rechtspositionen; kein künftiger Erwerb
- Art. 2 Abs. 1 GG: Allgemeine Handlungsfreiheit — Auffanggrundrecht
- Art. 3 Abs. 1 GG: Gleichheitssatz — kein Differenzierungsverbot; nur willkürliche Ungleichbehandlung verboten

**Persönlicher Schutzbereich:** Wer ist Träger des Grundrechts? Natürliche Personen; juristische Personen des Privatrechts (Art. 19 Abs. 3 GG), soweit das Grundrecht seinem Wesen nach anwendbar ist.

### Schritt 2 — Eingriff

**Klassischer Eingriff:** Finaler, unmittelbarer, rechtlicher, imperativer Akt staatlicher Gewalt.

**Moderner Eingriffsbegriff:** Auch mittelbar-faktische Beeinträchtigungen können Eingriff sein, wenn sie in ihrer Intensität einem Eingriff gleichkommen (BVerfG ständige Rechtsprechung — Osho, Glykol).

**Abgrenzung:** Nicht jede nachteilige staatliche Maßnahme ist ein Grundrechtseingriff. Rein fiskalisches Handeln, einfachgesetzliche Regelungen ohne Schutzbereichsbezug: kein Eingriff.

### Schritt 3 — Rechtfertigung

#### Schranken

Die Schranke des Grundrechts bestimmt, unter welchen Voraussetzungen ein Eingriff gerechtfertigt werden kann:
- Einfacher Gesetzesvorbehalt (z. B. Art. 2 Abs. 1 GG): Eingriff durch jedes formelle Gesetz möglich
- Qualifizierter Gesetzesvorbehalt (z. B. Art. 11 Abs. 2 GG): nur zum Schutz bestimmter Rechtsgüter
- Schrankenlos (absolute Grundrechte, z. B. Art. 1 Abs. 1 GG, Art. 4 Abs. 1 GG): kein Eingriff möglich, nur Schutzbereichsabgrenzung

#### Verhältnismäßigkeitsprüfung (Schranken-Schranke)

1. **Legitimer Zweck:** Staatliches Ziel muss verfassungsrechtlich erlaubt sein
2. **Geeignetheit:** Maßnahme muss Zweck fördern können
3. **Erforderlichkeit:** Kein gleich geeignetes, milderes Mittel
4. **Angemessenheit (Verhältnismäßigkeit i. e. S.):** Eingriff muss in angemessenem Verhältnis zur Zielerreichung stehen; Abwägung Eingriffsschwere vs. Gemeinwohlgewicht

## GRCh-Prüfung (Art. 51/52 GRCh)

**Anwendungsbereich Art. 51 Abs. 1 GRCh:** GRCh gilt für Organe der EU und für Mitgliedstaaten, wenn sie Unionsrecht durchführen. Rein nationales Handeln ohne Unionsbezug: GRCh nicht anwendbar.

**Schranken Art. 52 Abs. 1 GRCh:**
- Eingriff gesetzlich vorgesehen
- Wesensgehalt nicht angetastet
- Verhältnismäßigkeit (gleiche Prüfung wie GG: Eignung, Erforderlichkeit, Angemessenheit)

**Parallelprüfung:** Bei Sachverhalten mit Unionsbezug prüft das System GG und GRCh parallel und weist auf inhaltliche Parallelität oder Divergenz hin.

## Schutzpflichtdimension

Grundrechte verpflichten den Staat auch zum aktiven Schutz des Grundrechtsträgers gegenüber Dritten (BVerfG — Lüth; Handelsvertreterentscheidung). Das System fragt: Wird ein Schutzgebot staatlicher Seite geltend gemacht?

## Ausgabe

Strukturiertes Prüfungsprotokoll: Schutzbereich (eröffnet / nicht eröffnet), Eingriff (ja / nein / fraglich), Rechtfertigung (verhältnismäßig / unverhältnismäßig / fraglich), Ergebnis.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `kandidatenloesung-subsumtion-pruefen`

**Fokus:** Prueft abgegebene Klausur- oder Probandenloesungen auf Obersatz, Definition, Untersatz, Beleg, Ergebnis und typische Scheinkausalitaet. Gibt Korrekturvermerk mit Punkteindikation und Musterpassage.

# Kandidatenlösung auf Subsumtion prüfen

## Ziel

Dieser Skill prüft abgegebene Klausur- oder Kandidatenlösungen auf methodische Sauberkeit der Subsumtion. Er führt nicht schematisch durch, sondern erzwingt eine prüfbare Arbeitsspur: Sachverhalt, Norm, Tatbestandsmerkmal, Subsumtion, Gegenargument, Beleg und Ergebnis werden getrennt und bewertet.

## Prüfungsschema für Kandidatenlösungen

### Schritt 1 — Obersatz identifizieren

**Was prüfen:**
- Ist der Obersatz als Frage (Konjunktiv) formuliert? ("A könnte gegen B einen Anspruch auf X aus § Y haben.")
- Sind Parteien, Anspruchsrichtung und Rechtsfolge klar benannt?
- Wird der Obersatz mit "weil" oder "da" begonnen? (Fehler: Urteilsstil statt Gutachtenstil in der Einleitung)

**Häufige Fehler:**
- "A hat einen Anspruch auf X." → Indikativ im Obersatz (Urteilsstil-Fehler)
- Obersatz fehlt ganz → Subsumtion startet ohne Normbenennung
- Falsche Anspruchsgrundlage im Obersatz → gesamte Prüfung verfehlt

### Schritt 2 — Definition prüfen

**Was prüfen:**
- Ist für jedes streitige Tatbestandsmerkmal eine Definition vorhanden?
- Stammt die Definition aus einer Quelle (BGH, hM, Kommentar) oder aus dem Sachverhalt selbst?
- Ist die Definition abstrakt und allgemein (nicht sachverhaltsbezogen)?

**Häufige Fehler:**
- Definition fehlt: Tatsachen werden direkt unter die Norm subsumiert (Sprung-Subsumtion)
- Zirkuläre Definition: "Eine Sache ist ein körperlicher Gegenstand, denn hier liegt ein körperlicher Gegenstand vor."
- Definition stammt implizit aus der Falllösung, nicht aus einer Rechtsquelle

### Schritt 3 — Subsumtion prüfen

**Was prüfen:**
- Werden konkrete Tatsachen aus dem Sachverhalt unter die abstrakten Merkmale der Definition gehalten?
- Tritt der Kandidat wertend auf ("offensichtlich", "eindeutig") ohne Begründung?
- Werden Gegenargumente (Einwände, streitige Punkte) benannt und beantwortet?

**Häufige Fehler:**
- Wiederholung der Definition statt Anwendung auf den Sachverhalt
- Sachverhalt wird umformuliert, ohne unter die Merkmale subsumiert zu werden
- Behauptung ohne Akte: "Es liegt eine Pflichtverletzung vor." ohne Bezug auf konkrete Handlung

### Schritt 4 — Beleg und Beweis

**Was prüfen:**
- Wird für jede Tatsachenbehauptung ein Beleg aus dem Sachverhalt angegeben?
- Werden Beweisfragen angesprochen, wenn die Tatsachen streitig sind?
- Ist Beweislast korrekt zugeordnet?

### Schritt 5 — Ergebnis und Zwischen-/Gesamtergebnis

**Was prüfen:**
- Gibt es ein Zwischenergebnis je Tatbestandsmerkmal?
- Ist das Gesamtergebnis ein klares Indikativ? ("Ein Anspruch besteht." / "Ein Anspruch besteht nicht.")
- Wird im Ergebnis zwischen tatbestandlicher Erfüllung und Einreden unterschieden?

## Bewertungsmatrix

| Merkmal | Punkte (Indikation) | Häufiger Fehler |
|---|---|---|
| Obersatz Konjunktiv + Parteien + Norm | 1–2 | Indikativ oder Normfehler |
| Definition mit Quellenangabe | 2–3 | Fehlende oder zirkuläre Definition |
| Subsumtion Tatsachen unter Definition | 3–5 | Wiederholung statt Subsumtion |
| Zwischenergebnis je TBM | 1 | Fehlt; Konjunktiv statt Indikativ |
| Behandlung Gegenargumente | 1–2 | Streitstand übergangen |
| Gesamtergebnis Indikativ | 1 | Konjunktiv im Schluss |

## Red-Team-Fragen

- Welche Anspruchsgrundlage oder Norm ist verführerisch, aber falsch?
- Welche Tatsache wird im Sachverhalt nur behauptet, aber nicht belegt?
- Welche Rechtsfolge passt nicht zur gewählten Norm?
- Wo droht eine falsche Reihenfolge: BGB AT → BT; Primär → Sekundäranspruch; Vertrag → Delikt?

## Ausgabe

Korrekturvermerk mit Abschnittsmarkierungen (Rot/Gelb/Grün), Randbemerkungen, Punkteindikation und verbesserter Musterpassage für die schwächste Subsumtionspassage. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle; keine Blindzitate.

## Quellenregel

- Normtext live prüfen: gesetze-im-internet.de.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle (dejure.org, openjur.de, bgh.de).
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Korrekturvermerk, Prüfpfad, Lückenliste und Musterpassage.
