---
name: paragraphen-cic-vorvertragliche-ergaenzende
description: "Paragraphen CIC Vorvertragliche Ergaenzende: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Paragraphen CIC Vorvertragliche Ergaenzende

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Paragraphen CIC Vorvertragliche Ergaenzende** im Plugin Bgb At Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fristen-berechnung-paragraphen-186-193` | Klausurfall zur Fristenberechnung nach §§ 186 bis 193 BGB: Beginn einer Frist, Ereignisfrist und Kalenderfrist, Fristablauf am letzten Tag, Verlängerung bei Sonn- und Feiertagen nach § 193 BGB und Berechnung von Anfechtungs- und Verjährungsfristen. |
| `cic-vorvertragliche-pflichten-schnittstelle` | Klausurfall zu culpa in contrahendo nach §§ 280 Abs. 1 und 311 Abs. 2 BGB: Aufnahme von Vertragsverhandlungen, vorvertragliche Aufklärungs- und Schutzpflichten, Verschulden bei Vertragsschluss und Schadensersatz bei Abbruch oder Täuschung. |
| `ergaenzende-vertragsauslegung` | Klausurfall zur ergänzenden Vertragsauslegung nach §§ 133 und 157 BGB: planwidrige Regelungslücke feststellen, hypothetischen Parteiwillen ermitteln, Abgrenzung zu dispositiven Gesetzesnormen und Grenze der Auslegung zur richterlichen Rechtsfortbildung. |

## Arbeitsweg

Im Plugin Bgb At Pruefer gilt für **Paragraphen CIC Vorvertragliche Ergaenzende**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fristen-berechnung-paragraphen-186-193`

**Fokus:** Klausurfall zur Fristenberechnung nach §§ 186 bis 193 BGB: Beginn einer Frist, Ereignisfrist und Kalenderfrist, Fristablauf am letzten Tag, Verlängerung bei Sonn- und Feiertagen nach § 193 BGB und Berechnung von Anfechtungs- und Verjährungsfristen.

# Fristenberechnung — §§ 186 bis 193 BGB

## Mandantenfall

- Mandant fragt, ob seine Anfechtungserklärung vom letzten Freitag noch rechtzeitig war.
- Verjährungsfrist endet auf einen Sonntag — verlängert sich die Frist nach § 193 BGB?
- Klausurkonstellation: Angebotsfrist von zwei Wochen — konkreter Anfang und Ende berechnen.

## Erste Schritte

1. Art der Frist bestimmen: Ereignisfrist (nach einem Ereignis) oder Kalenderfrist (bestimmtes Datum).
2. Fristbeginn nach §§ 187 und 188 BGB: Wird der Anfangstag mitgezählt oder nicht?
3. Fristen nach Tagen, Wochen, Monaten oder Jahren: Berechnung nach §§ 188 und 189 BGB.
4. § 193 BGB: Ende der Frist an Sonn- oder Feiertag oder Samstag — Verlängerung auf nächsten Werktag.
5. Zeitpunkt des Fristablaufs: Ende des letzten Tages (24:00 Uhr).
6. Kontrolle: Rechenweg sichtbar machen, Ergebnis mit konkretem Datum angeben.

## Rechtsrahmen

- § 186 BGB: Anwendungsbereich der Fristenregeln auf Fristen und Termine.
- § 187 Abs. 1 BGB: Fristbeginn — Anfangstag wird nicht mitgezählt, wenn Frist ab einem Ereignis läuft.
- § 187 Abs. 2 BGB: Fristbeginn bei Anfang des Tages — Anfangstag wird mitgezählt.
- § 188 BGB: Fristende — bei Wochen- oder Monatsfristen der entsprechende Tag.
- § 189 BGB: Monats- und Jahresfristen bei fehlendem Endtag.
- § 193 BGB: Verlängerung bei Sonn- und Feiertagen sowie Samstagen.

## Prüfraster

1. Fristtyp bestimmen: Ereignisfrist oder Kalenderfrist?
2. Fristbeginn: § 187 Abs. 1 oder Abs. 2 BGB — Anfangstag mitgezählt oder nicht?
3. Fristlauf berechnen: Tage, Wochen, Monate oder Jahre.
4. Fristende: § 188 BGB — bei Wochen- und Monatsfristen entsprechender Wochentag oder Datum.
5. § 193 BGB: Fällt das Ende auf Samstag, Sonntag oder gesetzlichen Feiertag?
6. Verlängerung auf nächsten Werktag: neues Enddatum konkret benennen.
7. Ergebnis: Frist gewahrt oder abgelaufen mit Begründung und Rechenweg.

## Typische Fallstricke

- § 187 Abs. 1 BGB: Ereignisfristen zählen den Anfangstag nicht mit — häufiger Rechenfehler.
- § 193 BGB gilt nur für Samstag, wenn Fristablauf auf einen Samstag fällt, nicht als generelle Fristunterbrechung.
- Verjährungsfristen: § 199 BGB für Verjährungsbeginn kombiniert mit §§ 186 ff. BGB für Berechnung.
- Bundesweite vs. landesrechtliche Feiertage können Fristende unterschiedlich verschieben.

## Output

- Fristenberechnungsschema mit Rechenweg und konkretem Datum
- Übersicht §§ 186 bis 193 BGB mit Anwendungsbeispielen
- Gutachtenstil-Abschnitt zur Frist-Prüfung
- Klausurlösungsskizze: Frist gewahrt oder abgelaufen?

## Quellen

- [§ 187 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__187.html)
- [§ 188 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__188.html)
- [§ 193 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__193.html)
- [dejure.org § 193 BGB](https://dejure.org/gesetze/BGB/193.html)
- [§ 186 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__186.html)

## Vertiefung

### Grundregeln der Fristberechnung

§ 187 BGB: Bei Fristbeginn mit einem Ereignis oder Zeitpunkt (z.B. Zugang am 1.3.) beginnt die
Frist erst am nächsten Tag (2.3.) zu laufen. Die Frist selbst zählt nicht den Anfangstag.

§ 188 BGB: Das Fristende ist der letzte Tag der Frist. Bei Wochen- oder Monatsfristen ist es der
entsprechende Wochentag oder Monatstag. Fällt er auf einen Feiertag, verschiebt sich die Frist
nach § 193 BGB auf den nächsten Werktag.

### Rückwärtsberechnung

Bei Rückwärtsfristen (z.B. Kündigung muss 14 Tage vorher zugehen) gilt § 187 Abs. 2 BGB analog:
Der Tag des Ereignisses (Beendigungsdatum) zählt nicht, die Frist zählt rückwärts.

### Klausur-Checkliste Fristberechnung

- Fristbeginn: Mit Ereignis oder am Tag danach (§ 187 Abs. 1 oder 2 BGB)?
- Fristende: Letzter Tag der Woche/des Monats oder nach Tagen berechnet?
- Feiertags- und Wochenendregelung nach § 193 BGB beachtet?
- Anfechtungsfristen: § 121 BGB (unverzüglich) oder § 124 BGB (ein Jahr) — Fristbeginn?
- Verjährungsfristen: § 199 Abs. 1 BGB — Entstehung und Kenntnis als Doppelerfordernis?

## 2. `cic-vorvertragliche-pflichten-schnittstelle`

**Fokus:** Klausurfall zu culpa in contrahendo nach §§ 280 Abs. 1 und 311 Abs. 2 BGB: Aufnahme von Vertragsverhandlungen, vorvertragliche Aufklärungs- und Schutzpflichten, Verschulden bei Vertragsschluss und Schadensersatz bei Abbruch oder Täuschung.

# Culpa in contrahendo — Vorvertragliche Pflichten §§ 280 und 311 BGB

## Mandantenfall

- Mandant hat auf Grund falscher Angaben des Vertragspartners in Verhandlungen einen nachteiligen Vertrag geschlossen — cic-Anspruch?
- Verhandlungen wurden kurz vor Abschluss abgebrochen — kann Mandant Aufwendungsersatz fordern?
- Klausurkonstellation: Aufklärungspflichtverletzung bei Grundstückskauf neben kaufrechtlichem Gewährleistungsanspruch.

## Erste Schritte

1. Schuldverhältnis nach § 311 Abs. 2 BGB: Aufnahme von Vertragsverhandlungen oder ähnlicher Geschäftskontakt?
2. Pflichtverletzung bestimmen: Aufklärungspflichtverletzung, Täuschung, Abbruch ohne triftigen Grund?
3. Verschulden des Schuldners nach § 276 BGB (Vorsatz oder Fahrlässigkeit).
4. Schaden: Welche Aufwendungen hat der Gläubiger im Vertrauen auf Vertragsschluss gemacht?
5. Kausalität: Hätte der Gläubiger bei ordnungsgemäßer Aufklärung anders gehandelt?
6. Schadensersatz: negatives Interesse (Vertrauensschaden), nicht positives Interesse (Erfüllungsschaden).

## Rechtsrahmen

- § 311 Abs. 2 BGB: Schuldverhältnis durch Aufnahme von Vertragsverhandlungen.
- § 311 Abs. 3 BGB: Schuldverhältnis mit Dritten, die besonderes Vertrauen in Anspruch nehmen.
- § 280 Abs. 1 BGB: Schadensersatz wegen Pflichtverletzung des Schuldverhältnisses.
- § 241 Abs. 2 BGB: Schutz- und Rücksichtspflichten im Schuldverhältnis.
- § 123 BGB: arglistige Täuschung — cic tritt neben Anfechtungsrecht.
- § 249 BGB: Schadensersatz in Natur oder Geldersatz.

## Prüfraster

1. Vorvertragliches Schuldverhältnis nach § 311 Abs. 2 BGB entstanden?
2. Welche Pflicht nach § 241 Abs. 2 BGB wurde verletzt (Aufklärung, Schutz, Rücksicht)?
3. Verschulden: Vorsatz oder Fahrlässigkeit des Schuldners?
4. Schaden: Vertrauensschaden (Aufwendungen, entgangene Alternativgeschäfte)?
5. Kausalität zwischen Pflichtverletzung und Schaden?
6. Verhältnis zu § 123 BGB: cic und Anfechtung nebeneinander möglich?
7. Abbruch der Verhandlungen: triftiger Grund oder treuwidriger Abbruch?

## Typische Fallstricke

- cic ist kein Ersatz für kaufrechtliche Gewährleistung — Anspruchskonkurrenz klären.
- Vertrauensschaden umfasst nur negatives Interesse, nicht das Erfüllungsinteresse.
- § 311 Abs. 3 BGB erfordert besondere Vertrauensinanspruchnahme eines Dritten.
- Abbruch von Vertragsverhandlungen ist grundsätzlich erlaubt — nur treuwidriger Abbruch begründet cic.

## Output

- Gutachtenstil-Abschnitt zu cic nach §§ 280 und 311 BGB
- Anspruchskonkurrenz-Schema: cic neben § 123 BGB und kaufrechtlicher Gewährleistung
- Schadensberechnung: negatives Interesse mit Rechenweg
- Klausurlösungsskizze mit Schwerpunkt cic

## Quellen

- [§ 311 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__311.html)
- [§ 280 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__280.html)
- [§ 241 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__241.html)
- [dejure.org § 311 BGB](https://dejure.org/gesetze/BGB/311.html)
- [dejure.org § 280 BGB](https://dejure.org/gesetze/BGB/280.html)

## Vertiefung

### Systematik der cic

Die culpa in contrahendo (§§ 311 Abs. 2 und 241 Abs. 2 BGB) begründet ein vorvertragliches
Schuldverhältnis. Verletzt ein Beteiligter seine Rücksichtspflichten (§ 241 Abs. 2 BGB) bei
Vertragsanbahnung, entsteht ein Schadensersatzanspruch nach § 280 Abs. 1 BGB.

### Hauptfälle der cic

(1) Abbruch von Vertragsverhandlungen ohne triftigen Grund nach weit fortgeschrittenem Stadium,
(2) Pflichtverletzung durch fehlerhafte vorvertragliche Aufklärung,
(3) Verletzung von Schutzpflichten bei Anbahnung (Körperschäden im Geschäft des Vertragspartners).

### Klausur-Checkliste cic

- Vorvertragliches Schuldverhältnis nach § 311 Abs. 2 BGB begründet?
- Pflichtverletzung nach § 241 Abs. 2 BGB konkret benannt?
- Verschulden des Schädigers nach § 276 BGB (Fahrlässigkeit ausreichend)?
- Schaden: negatives oder positives Interesse — was verlangt der Geschädigte?
- Abgrenzung zur Anfechtung nach § 123 BGB: Beide Wege möglich?

## 3. `ergaenzende-vertragsauslegung`

**Fokus:** Klausurfall zur ergänzenden Vertragsauslegung nach §§ 133 und 157 BGB: planwidrige Regelungslücke feststellen, hypothetischen Parteiwillen ermitteln, Abgrenzung zu dispositiven Gesetzesnormen und Grenze der Auslegung zur richterlichen Rechtsfortbildung.

# Ergänzende Vertragsauslegung — §§ 133 und 157 BGB

## Mandantenfall

- Langzeitvertrag schweigt zur Preisanpassung bei außergewöhnlicher Kostenentwicklung — ergänzende Auslegung?
- Partnerschaftsvertrag enthält keine Regelung zur Kündigung — lückenlos ausgelegt oder gesetzliche Norm?
- Klausurkonstellation: AGB-Klausel ist unwirksam (§ 307 BGB) — kann die Lücke durch ergänzende Auslegung geschlossen werden?

## Erste Schritte

1. Regelungslücke feststellen: Vertrag schweigt zu einem relevanten Punkt.
2. Planwidrige Lücke prüfen: Haben die Parteien das Thema bewusst offengelassen oder nur vergessen?
3. Hypothetischer Parteiwille ermitteln: Was hätten vernünftige Parteien vereinbart?
4. Maßstab § 157 BGB: Treu und Glauben und Verkehrssitte.
5. Vorrang dispositiver Gesetzesnormen: Liegt eine passende gesetzliche Regelung vor?
6. Grenze: Keine Neuregelung durch ergänzende Auslegung — nur Schließung echter Lücke.

## Rechtsrahmen

- § 133 BGB: Auslegung — erforschung des wirklichen Willens.
- § 157 BGB: Vertragsauslegung nach Treu und Glauben und Verkehrssitte.
- § 306 BGB: AGB-Lücke — ergänzende Vertragsauslegung nach Unwirksamkeit einer Klausel.
- § 313 BGB: Störung der Geschäftsgrundlage — abzugrenzen von ergänzender Auslegung.
- § 242 BGB: Treu und Glauben als übergeordneter Auslegungsmaßstab.

## Prüfraster

1. Liegt eine Regelungslücke vor — Vertrag enthält keine Regelung für den eingetretenen Fall?
2. Planwidrige Lücke: Parteien haben das Thema nicht bedacht (nicht bewusst offengelassen)?
3. Hypothetischer Parteiwille: Was hätten redliche Parteien nach Treu und Glauben vereinbart?
4. Gesetzliche Regelung: Gibt es ein dispositives Gesetz, das die Lücke füllt?
5. AGB-Kontext nach § 306 BGB: Unwirksame Klausel — Lücke durch ergänzende Auslegung?
6. Grenze: Darf das Ergebnis den Vertrag nicht in eine andere Richtung lenken als die Parteien es wollten.
7. Abgrenzung zu § 313 BGB: Nicht jede Lücke ist eine Störung der Geschäftsgrundlage.

## Typische Fallstricke

- Ergänzende Auslegung ist kein Instrument für richterliche Rechtsfortbildung oder Vertragsneugestaltung.
- Bewusst offengelassene Lücken sind nicht planwidrig — keine ergänzende Auslegung möglich.
- Dispositives Recht hat Vorrang vor ergänzender Auslegung wenn eine passende Norm existiert.
- Im AGB-Recht sind die Anforderungen an ergänzende Auslegung strenger als bei Individualverträgen.

## Output

- Prüfungsschema ergänzende Vertragsauslegung: Lücke — planwidrig — hypothetischer Wille
- Abgrenzungstabelle: ergänzende Auslegung vs. dispositives Recht vs. § 313 BGB
- Gutachtenstil-Abschnitt zur Lückenschließung
- Klausurlösungsskizze mit Ergebnis

## Quellen

- [§ 133 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__133.html)
- [§ 157 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__157.html)
- [§ 306 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__306.html)
- [§ 313 BGB — gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__313.html)
- [dejure.org § 157 BGB](https://dejure.org/gesetze/BGB/157.html)

## Vertiefung

### Abgrenzung zur dispositiven Auslegung

Die ergänzende Vertragsauslegung nach §§ 133 und 157 BGB ist von der schlichten Auslegung
zu unterscheiden: Auslegung erschließt vorhandene Erklärungen. Ergänzende Auslegung füllt
echte Regelungslücken — Fälle, die die Parteien nicht bedacht haben.

### Hypothetischer Parteiwille

Maßstab der ergänzenden Auslegung ist der hypothetische Parteiwille: Was hätten die Parteien
vernünftigerweise vereinbart, wenn sie den Lückenfall bedacht hätten? Nicht was eine Partei
wollte, sondern was beide bei redlichem Vorgehen gewollt hätten.

### Klausur-Checkliste ergänzende Vertragsauslegung

- Echte Regelungslücke festgestellt (kein Dissens, kein offener Widerspruch)?
- Dispositives Gesetzesrecht als Lückenfüller ausreichend?
- Wenn nicht: Hypothetischer Parteiwille nach §§ 133 und 157 BGB ermittelbar?
- Ergebnis sachgerecht und für beide Parteien zumutbar?
- Abgrenzung zum Dissens: Haben Parteien die Lücke bewusst offengelassen?
