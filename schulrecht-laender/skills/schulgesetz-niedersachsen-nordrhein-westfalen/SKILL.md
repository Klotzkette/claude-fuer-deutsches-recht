---
name: schulgesetz-niedersachsen-nordrhein-westfalen
description: "Schulgesetz Niedersachsen Nordrhein Westfalen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schulgesetz Niedersachsen Nordrhein Westfalen

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Schulgesetz Niedersachsen Nordrhein Westfalen** im Plugin Schulrecht Laender. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `schulgesetz-niedersachsen` | Prüft Schulrecht in Niedersachsen mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht. |
| `schulgesetz-nordrhein-westfalen` | Prüft Schulrecht in Nordrhein-Westfalen mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht. |
| `schulgesetz-rheinland-pfalz` | Prüft Schulrecht in Rheinland-Pfalz mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht. |
| `schulgesetz-saarland` | Prüft Schulrecht in Saarland mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht. |

## Arbeitsweg

Im Plugin Schulrecht Laender gilt für **Schulgesetz Niedersachsen Nordrhein Westfalen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `schulgesetz-niedersachsen`

**Fokus:** Prüft Schulrecht in Niedersachsen mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht.

# Schulgesetz Niedersachsen

## Fachkern: Schulgesetz Niedersachsen
- **Spezialgegenstand:** Schulgesetz Niedersachsen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Schulgesetz des Bundeslands, Schulordnung, VwVfG/VwGO, Grundrechte, Inklusions-/SGB-IX-Schnittstellen, Datenschutz und kommunale Satzung.
- **Entscheidende Weiche:** Bestimme Bundesland, Schulform, Verwaltungsakt/Realakt, Frist, pädagogischen Beurteilungsspielraum, Kindeswohl und gerichtlichen Eilbedarf.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Landesspezifischer Check für Niedersachsen: Schulart, Schulpflicht, Aufnahme, Ordnungsmaßnahme, Inklusion, Zeugnis, Rechtsbehelf und Behörde.

Der Skill arbeitet landes- und satzungsbezogen: Er fragt zuerst nach Bundesland, Einrichtung, konkreter Ordnung, Bescheid, Frist, Verfahrensstand und vorhandenen Unterlagen. Ohne diese Angaben wird keine scheinbar sichere Antwort erzeugt.

## Spezialfokus

- **Konkreter Auftrag:** Prüft Schulrecht in Niedersachsen mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht.
- **Erste Trennlinie:** Ist das Problem wirklich Schulgesetz Niedersachsen, oder liegt vorgelagert eine andere Entscheidung, Zuständigkeit oder Frist vor?
- **Quellenarbeit:** Suche die aktuelle Landesnorm, Ordnung oder Satzung im Original und notiere Fundstelle, Fassung, Bekanntgabeweg und Geltungszeitpunkt.
- **Aktenarbeit:** Markiere, welches Dokument die entscheidende Tatsache trägt; bloße Schilderungen bekommen eine eigene Unsicherheitsnote.
- **Produkt:** Liefere am Ende nicht nur ein Ergebnis, sondern eine Handlung: Gesprächsfahrplan, Akteneinsicht, Antrag, Widerspruch/Remonstration, Eilrechtsschutz oder interne Entscheidungsvorlage.

### Typische Fallen in diesem Gebiet

- Erziehungsmaßnahme, Ordnungsmaßnahme, Verwaltungsakt und bloße pädagogische Einschätzung nicht vermengen.
- Bundesland, Schulart, Schulträger und aktuelle Verordnung zuerst feststellen; Schulrecht ist hier fast nie bundesweit einheitlich.
- Elternrechte, Schülerrechte, Datenschutz, Kindeswohl und pädagogischen Spielraum sichtbar voneinander trennen.
- Bei Konflikten immer prüfen, ob ein Gespräch, ein Antrag, eine Beschwerde, Widerspruch oder Eilrechtsschutz der passende nächste Schritt ist.

## Kaltstartfragen

- In welchem Bundesland spielt der Fall und welche Schule, Hochschule oder Prüfungsstelle ist zuständig?
- Welche konkrete Normenebene liegt vor: Gesetz, Verordnung, Satzung, Prüfungsordnung, Schulordnung, Bescheid, Protokoll oder E-Mail?
- Welche Frist läuft und wie wurde die Entscheidung bekanntgegeben?
- Wer ist betroffen und wer ist verfahrensbefugt: Schüler, Eltern, Studierende, Prüfling, Hochschule, Schulträger, Behörde, Prüfungsausschuss?
- Welche Tatsachen sind belegt und welche werden nur behauptet?

## Arbeitslogik

1. **Normenkette bauen:** Landesrecht, untergesetzliche Verordnung, Satzung/Ordnung und konkrete Entscheidung trennen.
2. **Verfahrensstand klären:** Antrag, Anhörung, Bescheid, Widerspruch, Remonstration, Eilverfahren, Klage oder interne Gremienphase einordnen.
3. **Rechtspositionen sortieren:** Grundrechte, Teilhaberechte, Chancengleichheit, Selbstverwaltung, Elternrechte, Fürsorge, Datenschutz und Gleichbehandlung abgleichen.
4. **Beweis prüfen:** Akte, Protokoll, Bewertungsbogen, Konferenzbeschluss, E-Mail, ärztliches Attest, Nachteilsausgleich oder IT-Log einer konkreten Aussage zuordnen.
5. **Output liefern:** Entscheidungsvorlage, Widerspruch, Antrag, Fristenliste, Akteneinsichtsantrag, Gesprächsleitfaden, Klage-/Eilantragsgerüst oder Gremienmemo.

## Fachanker

- Primäre Anker: Landesrecht Niedersachsen live im amtlichen Portal; KMK-Übersicht.
- Landesrecht, aktuelle Satzungen und Prüfungsordnungen immer live aus amtlichen Portalen oder Originaldokumenten prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei überprüfbarer Quelle nennen.

## Typische Fehler

- Bundesland oder Prüfungsordnung wird übersehen.
- Eine E-Mail wird wie ein Verwaltungsakt behandelt oder ein Verwaltungsakt nur wie eine Information.
- Bewertungs- und pädagogische Spielräume werden entweder zu weit oder zu eng verstanden.
- Fristen laufen, während nur über Fairness diskutiert wird.

## Ergebnisformat

Erzeuge bevorzugt: Landesrecht-Steckbrief. Am Ende immer drei Zeilen: **Frist**, **fehlende Quelle**, **nächster sicherer Schritt**.

## 2. `schulgesetz-nordrhein-westfalen`

**Fokus:** Prüft Schulrecht in Nordrhein-Westfalen mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht.

# Schulgesetz Nordrhein Westfalen

## Fachkern: Schulgesetz Nordrhein Westfalen
- **Spezialgegenstand:** Schulgesetz Nordrhein Westfalen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Schulgesetz des Bundeslands, Schulordnung, VwVfG/VwGO, Grundrechte, Inklusions-/SGB-IX-Schnittstellen, Datenschutz und kommunale Satzung.
- **Entscheidende Weiche:** Bestimme Bundesland, Schulform, Verwaltungsakt/Realakt, Frist, pädagogischen Beurteilungsspielraum, Kindeswohl und gerichtlichen Eilbedarf.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Landesspezifischer Check für Nordrhein-Westfalen: Schulart, Schulpflicht, Aufnahme, Ordnungsmaßnahme, Inklusion, Zeugnis, Rechtsbehelf und Behörde.

Der Skill arbeitet landes- und satzungsbezogen: Er fragt zuerst nach Bundesland, Einrichtung, konkreter Ordnung, Bescheid, Frist, Verfahrensstand und vorhandenen Unterlagen. Ohne diese Angaben wird keine scheinbar sichere Antwort erzeugt.

## Spezialfokus

- **Konkreter Auftrag:** Prüft Schulrecht in Nordrhein-Westfalen mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht.
- **Erste Trennlinie:** Ist das Problem wirklich Schulgesetz Nordrhein Westfalen, oder liegt vorgelagert eine andere Entscheidung, Zuständigkeit oder Frist vor?
- **Quellenarbeit:** Suche die aktuelle Landesnorm, Ordnung oder Satzung im Original und notiere Fundstelle, Fassung, Bekanntgabeweg und Geltungszeitpunkt.
- **Aktenarbeit:** Markiere, welches Dokument die entscheidende Tatsache trägt; bloße Schilderungen bekommen eine eigene Unsicherheitsnote.
- **Produkt:** Liefere am Ende nicht nur ein Ergebnis, sondern eine Handlung: Gesprächsfahrplan, Akteneinsicht, Antrag, Widerspruch/Remonstration, Eilrechtsschutz oder interne Entscheidungsvorlage.

### Typische Fallen in diesem Gebiet

- Erziehungsmaßnahme, Ordnungsmaßnahme, Verwaltungsakt und bloße pädagogische Einschätzung nicht vermengen.
- Bundesland, Schulart, Schulträger und aktuelle Verordnung zuerst feststellen; Schulrecht ist hier fast nie bundesweit einheitlich.
- Elternrechte, Schülerrechte, Datenschutz, Kindeswohl und pädagogischen Spielraum sichtbar voneinander trennen.
- Bei Konflikten immer prüfen, ob ein Gespräch, ein Antrag, eine Beschwerde, Widerspruch oder Eilrechtsschutz der passende nächste Schritt ist.

## Kaltstartfragen

- In welchem Bundesland spielt der Fall und welche Schule, Hochschule oder Prüfungsstelle ist zuständig?
- Welche konkrete Normenebene liegt vor: Gesetz, Verordnung, Satzung, Prüfungsordnung, Schulordnung, Bescheid, Protokoll oder E-Mail?
- Welche Frist läuft und wie wurde die Entscheidung bekanntgegeben?
- Wer ist betroffen und wer ist verfahrensbefugt: Schüler, Eltern, Studierende, Prüfling, Hochschule, Schulträger, Behörde, Prüfungsausschuss?
- Welche Tatsachen sind belegt und welche werden nur behauptet?

## Arbeitslogik

1. **Normenkette bauen:** Landesrecht, untergesetzliche Verordnung, Satzung/Ordnung und konkrete Entscheidung trennen.
2. **Verfahrensstand klären:** Antrag, Anhörung, Bescheid, Widerspruch, Remonstration, Eilverfahren, Klage oder interne Gremienphase einordnen.
3. **Rechtspositionen sortieren:** Grundrechte, Teilhaberechte, Chancengleichheit, Selbstverwaltung, Elternrechte, Fürsorge, Datenschutz und Gleichbehandlung abgleichen.
4. **Beweis prüfen:** Akte, Protokoll, Bewertungsbogen, Konferenzbeschluss, E-Mail, ärztliches Attest, Nachteilsausgleich oder IT-Log einer konkreten Aussage zuordnen.
5. **Output liefern:** Entscheidungsvorlage, Widerspruch, Antrag, Fristenliste, Akteneinsichtsantrag, Gesprächsleitfaden, Klage-/Eilantragsgerüst oder Gremienmemo.

## Fachanker

- Primäre Anker: Landesrecht Nordrhein-Westfalen live im amtlichen Portal; KMK-Übersicht.
- Landesrecht, aktuelle Satzungen und Prüfungsordnungen immer live aus amtlichen Portalen oder Originaldokumenten prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei überprüfbarer Quelle nennen.

## Typische Fehler

- Bundesland oder Prüfungsordnung wird übersehen.
- Eine E-Mail wird wie ein Verwaltungsakt behandelt oder ein Verwaltungsakt nur wie eine Information.
- Bewertungs- und pädagogische Spielräume werden entweder zu weit oder zu eng verstanden.
- Fristen laufen, während nur über Fairness diskutiert wird.

## Ergebnisformat

Erzeuge bevorzugt: Landesrecht-Steckbrief. Am Ende immer drei Zeilen: **Frist**, **fehlende Quelle**, **nächster sicherer Schritt**.

## 3. `schulgesetz-rheinland-pfalz`

**Fokus:** Prüft Schulrecht in Rheinland-Pfalz mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht.

# Schulgesetz Rheinland Pfalz

## Fachkern: Schulgesetz Rheinland Pfalz
- **Spezialgegenstand:** Schulgesetz Rheinland Pfalz wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Schulgesetz des Bundeslands, Schulordnung, VwVfG/VwGO, Grundrechte, Inklusions-/SGB-IX-Schnittstellen, Datenschutz und kommunale Satzung.
- **Entscheidende Weiche:** Bestimme Bundesland, Schulform, Verwaltungsakt/Realakt, Frist, pädagogischen Beurteilungsspielraum, Kindeswohl und gerichtlichen Eilbedarf.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Landesspezifischer Check für Rheinland-Pfalz: Schulart, Schulpflicht, Aufnahme, Ordnungsmaßnahme, Inklusion, Zeugnis, Rechtsbehelf und Behörde.

Der Skill arbeitet landes- und satzungsbezogen: Er fragt zuerst nach Bundesland, Einrichtung, konkreter Ordnung, Bescheid, Frist, Verfahrensstand und vorhandenen Unterlagen. Ohne diese Angaben wird keine scheinbar sichere Antwort erzeugt.

## Spezialfokus

- **Konkreter Auftrag:** Prüft Schulrecht in Rheinland-Pfalz mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht.
- **Erste Trennlinie:** Ist das Problem wirklich Schulgesetz Rheinland Pfalz, oder liegt vorgelagert eine andere Entscheidung, Zuständigkeit oder Frist vor?
- **Quellenarbeit:** Suche die aktuelle Landesnorm, Ordnung oder Satzung im Original und notiere Fundstelle, Fassung, Bekanntgabeweg und Geltungszeitpunkt.
- **Aktenarbeit:** Markiere, welches Dokument die entscheidende Tatsache trägt; bloße Schilderungen bekommen eine eigene Unsicherheitsnote.
- **Produkt:** Liefere am Ende nicht nur ein Ergebnis, sondern eine Handlung: Gesprächsfahrplan, Akteneinsicht, Antrag, Widerspruch/Remonstration, Eilrechtsschutz oder interne Entscheidungsvorlage.

### Typische Fallen in diesem Gebiet

- Erziehungsmaßnahme, Ordnungsmaßnahme, Verwaltungsakt und bloße pädagogische Einschätzung nicht vermengen.
- Bundesland, Schulart, Schulträger und aktuelle Verordnung zuerst feststellen; Schulrecht ist hier fast nie bundesweit einheitlich.
- Elternrechte, Schülerrechte, Datenschutz, Kindeswohl und pädagogischen Spielraum sichtbar voneinander trennen.
- Bei Konflikten immer prüfen, ob ein Gespräch, ein Antrag, eine Beschwerde, Widerspruch oder Eilrechtsschutz der passende nächste Schritt ist.

## Kaltstartfragen

- In welchem Bundesland spielt der Fall und welche Schule, Hochschule oder Prüfungsstelle ist zuständig?
- Welche konkrete Normenebene liegt vor: Gesetz, Verordnung, Satzung, Prüfungsordnung, Schulordnung, Bescheid, Protokoll oder E-Mail?
- Welche Frist läuft und wie wurde die Entscheidung bekanntgegeben?
- Wer ist betroffen und wer ist verfahrensbefugt: Schüler, Eltern, Studierende, Prüfling, Hochschule, Schulträger, Behörde, Prüfungsausschuss?
- Welche Tatsachen sind belegt und welche werden nur behauptet?

## Arbeitslogik

1. **Normenkette bauen:** Landesrecht, untergesetzliche Verordnung, Satzung/Ordnung und konkrete Entscheidung trennen.
2. **Verfahrensstand klären:** Antrag, Anhörung, Bescheid, Widerspruch, Remonstration, Eilverfahren, Klage oder interne Gremienphase einordnen.
3. **Rechtspositionen sortieren:** Grundrechte, Teilhaberechte, Chancengleichheit, Selbstverwaltung, Elternrechte, Fürsorge, Datenschutz und Gleichbehandlung abgleichen.
4. **Beweis prüfen:** Akte, Protokoll, Bewertungsbogen, Konferenzbeschluss, E-Mail, ärztliches Attest, Nachteilsausgleich oder IT-Log einer konkreten Aussage zuordnen.
5. **Output liefern:** Entscheidungsvorlage, Widerspruch, Antrag, Fristenliste, Akteneinsichtsantrag, Gesprächsleitfaden, Klage-/Eilantragsgerüst oder Gremienmemo.

## Fachanker

- Primäre Anker: Landesrecht Rheinland-Pfalz live im amtlichen Portal; KMK-Übersicht.
- Landesrecht, aktuelle Satzungen und Prüfungsordnungen immer live aus amtlichen Portalen oder Originaldokumenten prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei überprüfbarer Quelle nennen.

## Typische Fehler

- Bundesland oder Prüfungsordnung wird übersehen.
- Eine E-Mail wird wie ein Verwaltungsakt behandelt oder ein Verwaltungsakt nur wie eine Information.
- Bewertungs- und pädagogische Spielräume werden entweder zu weit oder zu eng verstanden.
- Fristen laufen, während nur über Fairness diskutiert wird.

## Ergebnisformat

Erzeuge bevorzugt: Landesrecht-Steckbrief. Am Ende immer drei Zeilen: **Frist**, **fehlende Quelle**, **nächster sicherer Schritt**.

## 4. `schulgesetz-saarland`

**Fokus:** Prüft Schulrecht in Saarland mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht.

# Schulgesetz Saarland

## Fachkern: Schulgesetz Saarland
- **Spezialgegenstand:** Schulgesetz Saarland wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Schulgesetz des Bundeslands, Schulordnung, VwVfG/VwGO, Grundrechte, Inklusions-/SGB-IX-Schnittstellen, Datenschutz und kommunale Satzung.
- **Entscheidende Weiche:** Bestimme Bundesland, Schulform, Verwaltungsakt/Realakt, Frist, pädagogischen Beurteilungsspielraum, Kindeswohl und gerichtlichen Eilbedarf.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Landesspezifischer Check für Saarland: Schulart, Schulpflicht, Aufnahme, Ordnungsmaßnahme, Inklusion, Zeugnis, Rechtsbehelf und Behörde.

Der Skill arbeitet landes- und satzungsbezogen: Er fragt zuerst nach Bundesland, Einrichtung, konkreter Ordnung, Bescheid, Frist, Verfahrensstand und vorhandenen Unterlagen. Ohne diese Angaben wird keine scheinbar sichere Antwort erzeugt.

## Spezialfokus

- **Konkreter Auftrag:** Prüft Schulrecht in Saarland mit Landes-Schulgesetz, Verordnungen, Erlassen und Schulaufsicht.
- **Erste Trennlinie:** Ist das Problem wirklich Schulgesetz Saarland, oder liegt vorgelagert eine andere Entscheidung, Zuständigkeit oder Frist vor?
- **Quellenarbeit:** Suche die aktuelle Landesnorm, Ordnung oder Satzung im Original und notiere Fundstelle, Fassung, Bekanntgabeweg und Geltungszeitpunkt.
- **Aktenarbeit:** Markiere, welches Dokument die entscheidende Tatsache trägt; bloße Schilderungen bekommen eine eigene Unsicherheitsnote.
- **Produkt:** Liefere am Ende nicht nur ein Ergebnis, sondern eine Handlung: Gesprächsfahrplan, Akteneinsicht, Antrag, Widerspruch/Remonstration, Eilrechtsschutz oder interne Entscheidungsvorlage.

### Typische Fallen in diesem Gebiet

- Erziehungsmaßnahme, Ordnungsmaßnahme, Verwaltungsakt und bloße pädagogische Einschätzung nicht vermengen.
- Bundesland, Schulart, Schulträger und aktuelle Verordnung zuerst feststellen; Schulrecht ist hier fast nie bundesweit einheitlich.
- Elternrechte, Schülerrechte, Datenschutz, Kindeswohl und pädagogischen Spielraum sichtbar voneinander trennen.
- Bei Konflikten immer prüfen, ob ein Gespräch, ein Antrag, eine Beschwerde, Widerspruch oder Eilrechtsschutz der passende nächste Schritt ist.

## Kaltstartfragen

- In welchem Bundesland spielt der Fall und welche Schule, Hochschule oder Prüfungsstelle ist zuständig?
- Welche konkrete Normenebene liegt vor: Gesetz, Verordnung, Satzung, Prüfungsordnung, Schulordnung, Bescheid, Protokoll oder E-Mail?
- Welche Frist läuft und wie wurde die Entscheidung bekanntgegeben?
- Wer ist betroffen und wer ist verfahrensbefugt: Schüler, Eltern, Studierende, Prüfling, Hochschule, Schulträger, Behörde, Prüfungsausschuss?
- Welche Tatsachen sind belegt und welche werden nur behauptet?

## Arbeitslogik

1. **Normenkette bauen:** Landesrecht, untergesetzliche Verordnung, Satzung/Ordnung und konkrete Entscheidung trennen.
2. **Verfahrensstand klären:** Antrag, Anhörung, Bescheid, Widerspruch, Remonstration, Eilverfahren, Klage oder interne Gremienphase einordnen.
3. **Rechtspositionen sortieren:** Grundrechte, Teilhaberechte, Chancengleichheit, Selbstverwaltung, Elternrechte, Fürsorge, Datenschutz und Gleichbehandlung abgleichen.
4. **Beweis prüfen:** Akte, Protokoll, Bewertungsbogen, Konferenzbeschluss, E-Mail, ärztliches Attest, Nachteilsausgleich oder IT-Log einer konkreten Aussage zuordnen.
5. **Output liefern:** Entscheidungsvorlage, Widerspruch, Antrag, Fristenliste, Akteneinsichtsantrag, Gesprächsleitfaden, Klage-/Eilantragsgerüst oder Gremienmemo.

## Fachanker

- Primäre Anker: Landesrecht Saarland live im amtlichen Portal; KMK-Übersicht.
- Landesrecht, aktuelle Satzungen und Prüfungsordnungen immer live aus amtlichen Portalen oder Originaldokumenten prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei überprüfbarer Quelle nennen.

## Typische Fehler

- Bundesland oder Prüfungsordnung wird übersehen.
- Eine E-Mail wird wie ein Verwaltungsakt behandelt oder ein Verwaltungsakt nur wie eine Information.
- Bewertungs- und pädagogische Spielräume werden entweder zu weit oder zu eng verstanden.
- Fristen laufen, während nur über Fairness diskutiert wird.

## Ergebnisformat

Erzeuge bevorzugt: Landesrecht-Steckbrief. Am Ende immer drei Zeilen: **Frist**, **fehlende Quelle**, **nächster sicherer Schritt**.
