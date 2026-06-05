---
name: amtsangemessene-alimentation
description: "Amtsangemessene Alimentation: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Amtsangemessene Alimentation

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Amtsangemessene Alimentation** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `amtsangemessene-alimentation` | Amtsangemessene Alimentation: Mindestabstand, Familienzuschläge, Nachzahlung, Widerspruch und Musterverfahren. |
| `amtsangemessene-alimentation-bverfg` | Skill zur Pruefung der amtsangemessenen Alimentation der Beamten Richter und Soldaten nach Art. 33 Abs. 5 GG. Skill arbeitet das fuenfstufige Pruefungsschema des BVerfG ab mit den Indikatoren Tarifabstand Preisentwicklung Versorgungsempfaenger Vergleich zu anderen Besoldungsgruppen Familienzuschlag und Mindestabstand zur Grundsicherung. Liefert Bausteine fuer Widerspruch gegen Besoldung und fuer Vorlageantrag an das BVerfG durch das Verwaltungsgericht. Klaert die Konstellationen Bund und Land seit der Foederalismusreform und die statischen Besoldungsanpassungen einzelner Laender. |
| `amtsangemessene-beschaeftigung` | Amtsangemessene Beschäftigung und Unterbeschäftigung: Statusamtgerechte Aufgaben, Degradierungsgefühl, Organisationsgewalt. |
| `anfaenger-modus-beamtenrecht` | Anfängerführung für Beamte, Richter, Bewerber und Anwälte: erklärt Begriffe, Verfahrenswege und typische Denkfehler ohne juristische Überwältigung. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Amtsangemessene Alimentation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `amtsangemessene-alimentation`

**Fokus:** Amtsangemessene Alimentation: Mindestabstand, Familienzuschläge, Nachzahlung, Widerspruch und Musterverfahren.


# Amtsangemessene Alimentation

## Aufgabe

Amtsangemessene Alimentation: Mindestabstand, Familienzuschläge, Nachzahlung, Widerspruch und Musterverfahren.

## Arbeitsweise

Prüfe Besoldungsjahr, Haushaltslage, Rechtsbehelfe, Widerspruchserfordernis, Ruhendstellung und vorhandene Musterverfahren. Keine Zahlen ohne aktuellen Live-Check.

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.

## Ausgabeformat

- Kurzantwort in drei Sätzen.
- Checkliste der fehlenden Tatsachen.
- Rechtliche Einordnung mit passenden Normgruppen.
- Nächste Schritte mit Fristen und Anlagen.
- Quellenhygiene: keine nicht überprüfbaren Fundstellen, keine Kommentar- oder Aufsatzblindzitate.

## 2. `amtsangemessene-alimentation-bverfg`

**Fokus:** Skill zur Pruefung der amtsangemessenen Alimentation der Beamten Richter und Soldaten nach Art. 33 Abs. 5 GG. Skill arbeitet das fuenfstufige Pruefungsschema des BVerfG ab mit den Indikatoren Tarifabstand Preisentwicklung Versorgungsempfaenger Vergleich zu anderen Besoldungsgruppen Familienzuschlag und Mindestabstand zur Grundsicherung. Liefert Bausteine fuer Widerspruch gegen Besoldung und fuer Vorlageantrag an das BVerfG durch das Verwaltungsgericht. Klaert die Konstellationen Bund und Land seit der Foederalismusreform und die statischen Besoldungsanpassungen einzelner Laender.


# Amtsangemessene Alimentation — Pruefschema BVerfG

## 1. Zweck und Anwendungsfall

Skill zur Pruefung, ob die Besoldung eines Beamten oder Richters dem Grundsatz der amtsangemessenen Alimentation aus Art. 33 Abs. 5 GG entspricht. Anwendung beim Widerspruch gegen die monatliche Besoldungsmitteilung mit dem Ziel der verfassungsgerichtlichen Vorlage durch das VG nach Art. 100 Abs. 1 GG.

## 2. Eingaben

- Besoldungsgruppe und Stufenstand
- Familienstand und Anzahl der unterhaltsberechtigten Kinder
- Bundesland oder Bund
- Besoldungsstrukturmaszgesetz / Besoldungstabelle
- Tarifentwicklung TV-L oder TVoeD vergleichbar
- Preisentwicklung Verbraucherpreisindex

## 3. Ablauf / Checkliste

### a) Erste Stufe — Pruefkriterien
- Das BVerfG hat in seiner staendigen Rechtsprechung mehrere Indikatoren etabliert, die im Zusammenwirken eine Vermutung der Unteralimentation begruenden koennen. Genannt werden u. a. Tarifentwicklung im oeffentlichen Dienst, Verbraucherpreisindex, Vergleich zur Grundsicherung, Abstand zur naechstniedrigeren Besoldungsgruppe, Familienzuschlag fuer das dritte und jedes weitere Kind.

### b) Zweite Stufe — Gesamtbetrachtung
- Auf der zweiten Stufe ist eine Gesamtbetrachtung anzustellen, die auch qualitative Aspekte (Statusrelevanz, Mindestabstand zur Grundsicherung, Hergebrachte Grundsaetze) einbezieht.

### c) Dritte Stufe — Rechtfertigung
- Der Gesetzgeber kann Eingriffe nur in engen Grenzen rechtfertigen.

### d) Widerspruch und Rechtsweg
- Widerspruch gegen die monatliche Bezuegemitteilung (laenderspezifisch, ggf. Antrag auf erneute Festsetzung).
- Klage zum VG; Aussetzung des Verfahrens und Vorlage an das BVerfG nach Art. 100 Abs. 1 GG, wenn das VG von der Verfassungswidrigkeit ueberzeugt ist.

### e) Foederalismusreform 2006
- Die Besoldung der Landes- und Kommunalbeamten ist seit der Foederalismusreform Sache der Laender. Daraus folgen unterschiedliche Anpassungspfade. Verfassungswidrigkeit ist landesspezifisch zu pruefen.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 5, Art. 100 Abs. 1 GG; BBesG; Landesbesoldungsgesetze.
- Rspr.: BVerfG zur amtsangemessenen Alimentation (Leitentscheidungen zu R-Besoldung und A-Besoldung) — Quellenanker unten; konkrete Entscheidung in amtlicher oder freier Quelle prüfen (verbreitet zitierte Entscheidungen mit Aktenzeichen wie "2 BvL 17/09" oder "2 BvL 4/18" im konkreten Mandat in amtlicher Quelle pruefen).
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Widerspruchsschrift gegen Besoldungsfestsetzung.
- Memoraster mit den BVerfG-Indikatoren.
- Vorbereitendes Schreiben fuer Klage am VG mit Antrag auf Vorlage an das BVerfG.

## 6. Verifizierte Quellenanker

- BVerfG, 05.05.2015 - 2 BvL 17/09 u.a.: R-Besoldung Sachsen-Anhalt; Parameterprüfung zur amtsangemessenen Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 4/18: R-Besoldung Berlin; Mindestabstand und Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 6/17 u.a.: kinderreiche Richterfamilien und Familienzuschlag.
- BVerfG, 17.09.2025 - 2 BvL 20/17 u.a.: Berliner A-Besoldung; Prekaritätsschwelle und Dreischritt.
- Seit der Föderalismusreform 2006 ist Landesbesoldung landesrechtlich zu prüfen; BBesG nur für Bund/Soldaten und fortgeltende Sonderlagen.
- Für Stufen, Auslandsdienstbezüge, Erschwerniszulagen und Mehrarbeit zusätzlich aktuelle Spezialnormen live prüfen; die BVerfG-Linie ersetzt keine Fachnormprüfung.

## 7. Beispiel (Kurzfassung)

R1-Richterin in einem Bundesland mit alter Besoldungstabelle, drei Kinder. Skill liefert Indikatorentabelle, Widerspruchsentwurf mit Antrag auf Vorlage an das BVerfG sowie Hinweis auf laufende Verfahren in der eigenen Besoldungsgruppe.

## 3. `amtsangemessene-beschaeftigung`

**Fokus:** Amtsangemessene Beschäftigung und Unterbeschäftigung: Statusamtgerechte Aufgaben, Degradierungsgefühl, Organisationsgewalt.


# Amtsangemessene Beschaeftigung

## Aufgabe

Amtsangemessene Beschäftigung und Unterbeschäftigung: Statusamtgerechte Aufgaben, Degradierungsgefühl, Organisationsgewalt.

## Arbeitsweise

Vergleiche Statusamt, Besoldungsgruppe und tatsächliche Aufgaben. Dokumentiere Tätigkeitsprofil, Dauer, dienstliche Gründe und mögliche Abhilfe.

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.

## Ausgabeformat

- Kurzantwort in drei Sätzen.
- Checkliste der fehlenden Tatsachen.
- Rechtliche Einordnung mit passenden Normgruppen.
- Nächste Schritte mit Fristen und Anlagen.
- Quellenhygiene: keine nicht überprüfbaren Fundstellen, keine Kommentar- oder Aufsatzblindzitate.

## 4. `anfaenger-modus-beamtenrecht`

**Fokus:** Anfängerführung für Beamte, Richter, Bewerber und Anwälte: erklärt Begriffe, Verfahrenswege und typische Denkfehler ohne juristische Überwältigung.


# Anfaenger Modus Beamtenrecht

## Aufgabe

Anfängerführung für Beamte, Richter, Bewerber und Anwälte: erklärt Begriffe, Verfahrenswege und typische Denkfehler ohne juristische Überwältigung.

## Arbeitsweise

Übersetze das Problem in einfache Schritte: Was ist ein Verwaltungsakt, was ist eine dienstliche Maßnahme, wann braucht man Widerspruch, wann Eilantrag, wann nur Gegenvorstellung? Halte jede Ausgabe dreistufig: Kurzantwort, Was jetzt zu tun ist, Warum das rechtlich so ist.

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.

## Ausgabeformat

- Kurzantwort in drei Sätzen.
- Checkliste der fehlenden Tatsachen.
- Rechtliche Einordnung mit passenden Normgruppen.
- Nächste Schritte mit Fristen und Anlagen.
- Quellenhygiene: keine nicht überprüfbaren Fundstellen, keine Kommentar- oder Aufsatzblindzitate.
