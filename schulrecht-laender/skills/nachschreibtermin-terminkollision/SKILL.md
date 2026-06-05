---
name: nachschreibtermin-terminkollision
description: "Nachschreibtermin Terminkollision: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Nachschreibtermin Terminkollision

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Nachschreibtermin Terminkollision** im Plugin Schulrecht Laender. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nachschreibtermin-terminkollision` | Prüft Nachschreiben, Terminüberschneidung, Krankheit und Chancengleichheit. |
| `nachteilsausgleich-lrs-dyskalkulie` | Prüft LRS/Dyskalkulie-spezifische Maßnahmen. |
| `nachteilsausgleich-schule` | Prüft Nachteilsausgleich in Unterricht und Prüfungen. |
| `notenschutz-und-bewertung` | Prüft Notenschutz, Bewertung und Transparenz. |

## Arbeitsweg

Im Plugin Schulrecht Laender gilt für **Nachschreibtermin Terminkollision**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `nachschreibtermin-terminkollision`

**Fokus:** Prüft Nachschreiben, Terminüberschneidung, Krankheit und Chancengleichheit.

# Nachschreibtermin und Terminkollision

## Fachkern: Nachschreibtermin und Terminkollision
- **Spezialgegenstand:** Nachschreibtermin und Terminkollision wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Schulgesetz des Bundeslands, Schulordnung, VwVfG/VwGO, Grundrechte, Inklusions-/SGB-IX-Schnittstellen, Datenschutz und kommunale Satzung.
- **Entscheidende Weiche:** Bestimme Bundesland, Schulform, Verwaltungsakt/Realakt, Frist, pädagogischen Beurteilungsspielraum, Kindeswohl und gerichtlichen Eilbedarf.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Dieser Skill vertieft ein konkretes Problem im Schulrecht. Er ist für Eltern, Schülerinnen und Schüler, Schulleitung, Schulträger oder Behörde gedacht und soll aus unvollständigen Akten schnell eine belastbare Prüfspur machen.

## Spezialfokus

- **Konkreter Auftrag:** Prüft Nachschreiben, Terminüberschneidung, Krankheit und Chancengleichheit.
- **Erste Trennlinie:** Ist das Problem wirklich Nachschreibtermin und Terminkollision, oder liegt vorgelagert eine andere Entscheidung, Zuständigkeit oder Frist vor?
- **Quellenarbeit:** Suche die aktuelle Landesnorm, Ordnung oder Satzung im Original und notiere Fundstelle, Fassung, Bekanntgabeweg und Geltungszeitpunkt.
- **Aktenarbeit:** Markiere, welches Dokument die entscheidende Tatsache trägt; bloße Schilderungen bekommen eine eigene Unsicherheitsnote.
- **Produkt:** Liefere am Ende nicht nur ein Ergebnis, sondern eine Handlung: Gesprächsfahrplan, Akteneinsicht, Antrag, Widerspruch/Remonstration, Eilrechtsschutz oder interne Entscheidungsvorlage.

### Typische Fallen in diesem Gebiet

- Erziehungsmaßnahme, Ordnungsmaßnahme, Verwaltungsakt und bloße pädagogische Einschätzung nicht vermengen.
- Bundesland, Schulart, Schulträger und aktuelle Verordnung zuerst feststellen; Schulrecht ist hier fast nie bundesweit einheitlich.
- Elternrechte, Schülerrechte, Datenschutz, Kindeswohl und pädagogischen Spielraum sichtbar voneinander trennen.
- Bei Konflikten immer prüfen, ob ein Gespräch, ein Antrag, eine Beschwerde, Widerspruch oder Eilrechtsschutz der passende nächste Schritt ist.

## Kaltstartfragen

- In welchem Bundesland und bei welcher konkreten Einrichtung spielt der Fall?
- Welche Entscheidung, Maßnahme, Satzung, Ordnung, E-Mail oder welches Protokoll liegt wirklich vor?
- Welche Frist läuft, wann wurde bekanntgegeben und gibt es bereits Widerspruch, Remonstration, Antrag, Beschwerde oder Eilverfahren?
- Welche Tatsachen sind durch Aktenstücke belegt und welche sind nur Erzählstand?
- Welches Ziel soll erreicht werden: Aufhebung, Neubescheidung, Duldung, Gesprächslösung, Vergleich, Akteneinsicht oder nur Risikoeinschätzung?

## Prüfprogramm

1. **Normhierarchie trennen:** Landesschulgesetz, Schulverordnung, Erlasslage, Schulordnung, Bescheid und VwGO nicht vermischen; die konkrete Ordnung und den Bescheid immer zuerst lesen.
2. **Zuständigkeit und Verfahren prüfen:** Wer durfte entscheiden, wer musste beteiligt werden, welches Gremium war zuständig und welche Anhörung fehlt möglicherweise?
3. **Materielle Grenze bestimmen:** Ermessen, Beurteilungs- oder Bewertungsspielraum respektieren, aber Willkür, Verfahrensfehler, Gleichbehandlung, Grundrechte und Verhältnismäßigkeit sauber herausarbeiten.
4. **Beweisroute bauen:** Aktenstück, Protokoll, Chat, E-Mail, Attest, Bewertungsbogen, Satzungsauszug oder amtliche Quelle jeder Tatsachenbehauptung zuordnen.
5. **Nächsten Schritt liefern:** knappe Lageeinschätzung, Fristenliste, Antrag, Widerspruch, Remonstration, Eilantragsgerüst, Gesprächsleitfaden oder Beschluss-/Bescheidkritik.

## Fachliche Leitplanken

- Landesrecht und Satzungsrecht sind dynamisch; vor einer konkreten Ausgabe müssen aktuelle amtliche Quellen oder Originalordnungen geprüft werden.
- Rechtsprechung nur zitieren, wenn Gericht, Datum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.
- Keine pauschalen Aussagen wie "immer rechtswidrig" oder "pädagogisch nicht angreifbar"; entscheidend sind Verfahrensspur, Dokumentation, Gleichbehandlung und konkrete Rechtsgrundlage.

## Output-Muster

- **Sofortlage:** Was ist entschieden, was läuft, was droht?
- **Angriffspunkte:** Zuständigkeit, Verfahren, Begründung, Tatsachenbasis, Ermessen/Bewertungsspielraum, Verhältnismäßigkeit.
- **Dokumentenbedarf:** fehlende Akten, Protokolle, Ordnungen, Atteste, Gremienbeschlüsse und Zustellnachweise.
- **Entwurf:** präziser Antrag oder Schriftsatzbaustein mit Frist, Ziel und Begründung.

## 2. `nachteilsausgleich-lrs-dyskalkulie`

**Fokus:** Prüft LRS/Dyskalkulie-spezifische Maßnahmen.

# Nachteilsausgleich Lrs Dyskalkulie

## Fachkern: Nachteilsausgleich Lrs Dyskalkulie
- **Spezialgegenstand:** Nachteilsausgleich Lrs Dyskalkulie wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Schulgesetz des Bundeslands, Schulordnung, VwVfG/VwGO, Grundrechte, Inklusions-/SGB-IX-Schnittstellen, Datenschutz und kommunale Satzung.
- **Entscheidende Weiche:** Bestimme Bundesland, Schulform, Verwaltungsakt/Realakt, Frist, pädagogischen Beurteilungsspielraum, Kindeswohl und gerichtlichen Eilbedarf.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Diagnostik, Förderung, Bewertung, Notenschutz, Zeugnisbemerkung und Landesunterschiede.

Der Skill arbeitet landes- und satzungsbezogen: Er fragt zuerst nach Bundesland, Einrichtung, konkreter Ordnung, Bescheid, Frist, Verfahrensstand und vorhandenen Unterlagen. Ohne diese Angaben wird keine scheinbar sichere Antwort erzeugt.

## Spezialfokus

- **Konkreter Auftrag:** Prüft LRS/Dyskalkulie-spezifische Maßnahmen.
- **Erste Trennlinie:** Ist das Problem wirklich Nachteilsausgleich Lrs Dyskalkulie, oder liegt vorgelagert eine andere Entscheidung, Zuständigkeit oder Frist vor?
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

- Primäre Anker: Landeserlasse; Schulrecht.
- Landesrecht, aktuelle Satzungen und Prüfungsordnungen immer live aus amtlichen Portalen oder Originaldokumenten prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei überprüfbarer Quelle nennen.

## Typische Fehler

- Bundesland oder Prüfungsordnung wird übersehen.
- Eine E-Mail wird wie ein Verwaltungsakt behandelt oder ein Verwaltungsakt nur wie eine Information.
- Bewertungs- und pädagogische Spielräume werden entweder zu weit oder zu eng verstanden.
- Fristen laufen, während nur über Fairness diskutiert wird.

## Ergebnisformat

Erzeuge bevorzugt: LRS/Dyskalkulie-Antrag. Am Ende immer drei Zeilen: **Frist**, **fehlende Quelle**, **nächster sicherer Schritt**.

## 3. `nachteilsausgleich-schule`

**Fokus:** Prüft Nachteilsausgleich in Unterricht und Prüfungen.

# Nachteilsausgleich Schule

## Fachkern: Nachteilsausgleich Schule
- **Spezialgegenstand:** Nachteilsausgleich Schule wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Schulgesetz des Bundeslands, Schulordnung, VwVfG/VwGO, Grundrechte, Inklusions-/SGB-IX-Schnittstellen, Datenschutz und kommunale Satzung.
- **Entscheidende Weiche:** Bestimme Bundesland, Schulform, Verwaltungsakt/Realakt, Frist, pädagogischen Beurteilungsspielraum, Kindeswohl und gerichtlichen Eilbedarf.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

LRS, Dyskalkulie, ADHS, Behinderung, chronische Krankheit, Atteste, Maßnahme und Dokumentation.

Der Skill arbeitet landes- und satzungsbezogen: Er fragt zuerst nach Bundesland, Einrichtung, konkreter Ordnung, Bescheid, Frist, Verfahrensstand und vorhandenen Unterlagen. Ohne diese Angaben wird keine scheinbar sichere Antwort erzeugt.

## Spezialfokus

- **Konkreter Auftrag:** Prüft Nachteilsausgleich in Unterricht und Prüfungen.
- **Erste Trennlinie:** Ist das Problem wirklich Nachteilsausgleich Schule, oder liegt vorgelagert eine andere Entscheidung, Zuständigkeit oder Frist vor?
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

- Primäre Anker: Landesschulrecht; Art. 3 GG; Teilhaberecht.
- Landesrecht, aktuelle Satzungen und Prüfungsordnungen immer live aus amtlichen Portalen oder Originaldokumenten prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei überprüfbarer Quelle nennen.

## Typische Fehler

- Bundesland oder Prüfungsordnung wird übersehen.
- Eine E-Mail wird wie ein Verwaltungsakt behandelt oder ein Verwaltungsakt nur wie eine Information.
- Bewertungs- und pädagogische Spielräume werden entweder zu weit oder zu eng verstanden.
- Fristen laufen, während nur über Fairness diskutiert wird.

## Ergebnisformat

Erzeuge bevorzugt: Nachteilsausgleichsantrag. Am Ende immer drei Zeilen: **Frist**, **fehlende Quelle**, **nächster sicherer Schritt**.

## 4. `notenschutz-und-bewertung`

**Fokus:** Prüft Notenschutz, Bewertung und Transparenz.

# Notenschutz Und Bewertung

## Fachkern: Notenschutz Und Bewertung
- **Spezialgegenstand:** Notenschutz Und Bewertung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** Schulgesetz des Bundeslands, Schulordnung, VwVfG/VwGO, Grundrechte, Inklusions-/SGB-IX-Schnittstellen, Datenschutz und kommunale Satzung.
- **Entscheidende Weiche:** Bestimme Bundesland, Schulform, Verwaltungsakt/Realakt, Frist, pädagogischen Beurteilungsspielraum, Kindeswohl und gerichtlichen Eilbedarf.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Wofür dieser Arbeitsgang da ist

Was ist Nachteilsausgleich, was ist Notenschutz, was muss im Zeugnis stehen und was nicht.

Der Skill arbeitet landes- und satzungsbezogen: Er fragt zuerst nach Bundesland, Einrichtung, konkreter Ordnung, Bescheid, Frist, Verfahrensstand und vorhandenen Unterlagen. Ohne diese Angaben wird keine scheinbar sichere Antwort erzeugt.

## Spezialfokus

- **Konkreter Auftrag:** Prüft Notenschutz, Bewertung und Transparenz.
- **Erste Trennlinie:** Ist das Problem wirklich Notenschutz Und Bewertung, oder liegt vorgelagert eine andere Entscheidung, Zuständigkeit oder Frist vor?
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

- Primäre Anker: Landesschulrecht Notenschutz; Prüfungsrecht.
- Landesrecht, aktuelle Satzungen und Prüfungsordnungen immer live aus amtlichen Portalen oder Originaldokumenten prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei überprüfbarer Quelle nennen.

## Typische Fehler

- Bundesland oder Prüfungsordnung wird übersehen.
- Eine E-Mail wird wie ein Verwaltungsakt behandelt oder ein Verwaltungsakt nur wie eine Information.
- Bewertungs- und pädagogische Spielräume werden entweder zu weit oder zu eng verstanden.
- Fristen laufen, während nur über Fairness diskutiert wird.

## Ergebnisformat

Erzeuge bevorzugt: Bewertungsvermerk. Am Ende immer drei Zeilen: **Frist**, **fehlende Quelle**, **nächster sicherer Schritt**.
