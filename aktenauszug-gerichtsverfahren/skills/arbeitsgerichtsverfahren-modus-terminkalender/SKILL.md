---
name: arbeitsgerichtsverfahren-modus-terminkalender
description: "Arbeitsgerichtsverfahren Modus Terminkalender: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Arbeitsgerichtsverfahren Modus Terminkalender

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Arbeitsgerichtsverfahren Modus Terminkalender** im Plugin Aktenauszug zivilgerichtlicher Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `arbeitsgerichtsverfahren-modus` | Aktenauszug für ArbGG-Verfahren erstellen: Guetetermin Kammerverfahren Urteilsverfahren Beschlussverfahren. KSchG-Dreiwochenfrist § 4 KSchG Berufung § 64 ArbGG Revision § 72 ArbGG. Normen ArbGG §§ 2 54 64 72 KSchG §§ 1 4 9. Prüfraster Fristen-Spezifika arbeitsgerichtliche Besonderheiten BAG-Leitsaetze. Output ArbGG-spezifischer Aktenauszug. Abgrenzung zu zivilprozess-modus (ZPO) und sozialgerichtsverfahren-modus (SGG). |
| `fristen-und-terminkalender` | Anwalt will alle prozessrelevanten Fristen und Termine im Aktenauszug hervorheben: Klagefrist Berufungsfrist Begründungsfrist Verkündungstermin Vollziehungsfrist. Normen §§ 222 517 520 548 ZPO. Prüfraster Vollständigkeit Frist-Berechnung Hervorhebung Fehler-Scan. Output Fristen-Box Fristen-Tabelle. Abgrenzung zu verfahrenschronologie (Prozessschritte) und mittelstand-ma-fristen-cp-kalender (M&A-Fristen). |
| `sozialgerichtsverfahren-modus` | Aktenauszug für SGG-Verfahren erstellen: Klage Berufung §§ 143 ff. SGG Eilantrag § 86b SGG Widerspruchsverfahren. Amtsermittlungsgrundsatz Sozialversicherungs-Leistungsarten. Normen SGG §§ 51 77 86b 143. Prüfraster SGG-spezifische Fristen Vorverfahrens-Prüfung Leistungsarten. Output SGG-spezifischer Aktenauszug. Abgrenzung zu verwaltungsprozess-modus (VwGO) und arbeitsgerichtsverfahren-modus (ArbGG). |

## Arbeitsweg

Im Plugin Aktenauszug zivilgerichtlicher Verfahren gilt für **Arbeitsgerichtsverfahren Modus Terminkalender**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `arbeitsgerichtsverfahren-modus`

**Fokus:** Aktenauszug für ArbGG-Verfahren erstellen: Guetetermin Kammerverfahren Urteilsverfahren Beschlussverfahren. KSchG-Dreiwochenfrist § 4 KSchG Berufung § 64 ArbGG Revision § 72 ArbGG. Normen ArbGG §§ 2 54 64 72 KSchG §§ 1 4 9. Prüfraster Fristen-Spezifika arbeitsgerichtliche Besonderheiten BAG-Leitsaetze. Output ArbGG-spezifischer Aktenauszug. Abgrenzung zu zivilprozess-modus (ZPO) und sozialgerichtsverfahren-modus (SGG).

# Arbeitsgerichtsverfahren-Modus (ArbGG)

## Zweck

Dieser Modus-Skill aktiviert die verfahrensspezifischen Einstellungen für arbeitsgerichtliche Verfahren nach dem Arbeitsgerichtsgesetz (ArbGG). Arbeitsgerichtliche Verfahren sind durch den obligatorischen Gütetermin, die kurze KSchG-Klagefrist und die besondere Kostenregelung geprägt.

## Triage — kläre vor Aktivierung des Modus

1. Urteilsverfahren (§§ 46 ff. ArbGG) oder Beschlussverfahren (§§ 80 ff. ArbGG)?
2. Kündigungsschutzklage? → Klagefrist 3 Wochen ab Zugang (§ 4 KSchG) — sofort prüfen!
3. Instanz: Arbeitsgericht / LAG / BAG?
4. Liegt ein Güteterminprotokoll in der Akte?
5. Massenentlassung i.S.v. § 17 KSchG? (Anzeige bei Agentur für Arbeit?)

## Zentrale Normen (ArbGG / KSchG)

- § 4 KSchG — Klagefrist 3 Wochen; § 7 KSchG — Heilungsfiktion bei Fristversäumnis
- § 5 KSchG — Nachträgliche Klagezulassung (enge Voraussetzungen)
- § 1 KSchG — Soziale Rechtfertigung der Kündigung (Anwendbarkeit: § 23 KSchG)
- § 102 BetrVG — Betriebsratsanhörung vor Kündigung (Formerfordernis)
- §§ 46-49 ArbGG — Urteilsverfahren; § 54 ArbGG — Güteversuch
- §§ 64-74 ArbGG — Berufung und Revision beim LAG/BAG
- § 80-90 ArbGG — Beschlussverfahren; § 83 ArbGG — Untersuchungsgrundsatz
- § 12a ArbGG — Kein Anwaltskostenersatz in 1. Instanz

## Rechtsprechung (BAG — aktuelle Leitsätze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verfahrensarten

### Urteilsverfahren (§§ 46 ff. ArbGG)

Für bürgerliche Rechtsstreitigkeiten zwischen Arbeitnehmern und Arbeitgebern.

**Typischer Ablauf:**

1. Klageeingang
2. Gütetermin (§ 54 ArbGG) — obligatorisch, schnell angesetzt
3. Bei Scheitern: Kammertermin (Hauptverhandlung)
4. Urteil
5. Berufung zum Landesarbeitsgericht (§ 64 ArbGG)
6. Revision zum Bundesarbeitsgericht (§ 72 ArbGG)

### Beschlussverfahren (§§ 80 ff. ArbGG)

Für kollektivrechtliche Streitigkeiten (Betriebsverfassung, Mitbestimmung).

Beteiligte: Arbeitgeber / Betriebsrat / Gewerkschaft. Keine Parteien im zivilprozessualen Sinne — im Aktenauszug "Antragsteller" und "Antragsgegner" verwenden.

## Kritische Fristen (ArbGG / KSchG)

| Frist | Norm | Dauer | Besonderheit |
|---|---|---|---|
| Kündigungsschutzklage | § 4 KSchG | 3 Wochen | ab Zugang Kündigung — NOTFRIST |
| Berufungsfrist | § 66 Abs. 1 ArbGG | 1 Monat | ab Zustellung Urteil |
| Berufungsbegründungsfrist | § 66 Abs. 1 ArbGG | 2 Monate | ab Zustellung Urteil |
| Revisionsfrist | § 74 Abs. 1 ArbGG | 1 Monat | ab Zustellung Urteil |

**Besondere Hervorhebung:** Die Dreiwochenfrist des § 4 KSchG ist absolut — bei Versäumnis gilt die Kündigung als wirksam (§ 7 KSchG), selbst wenn sie materiell unwirksam wäre. Nachträgliche Zulassung nur unter engen Voraussetzungen (§ 5 KSchG).

## Besonderheiten Gütetermin

- Gütetermin findet regelmäßig wenige Wochen nach Klageeingang statt
- Richter versucht aktiv Vergleich herbeizuführen
- Bei Einigung im Gütetermin: Prozessvergleich (§ 794 Abs. 1 Nr. 1 ZPO)
- Im Aktenauszug: Güteterminsdatum und Ergebnis (Einigung / Scheitern) hervorheben
- Abfindungserwartung Faustformel: 0,5 Bruttomonatsgehaelter pro Beschaeftigungsjahr

## Besonderheiten Beschlussverfahren

- Untersuchungsgrundsatz (§ 83 ArbGG) — Gericht ermittelt von Amts wegen
- Beteiligte können unbeschränkt Anträge stellen
- Rechtskraft des Beschlusses nur für Beteiligte

## Kostenrecht (§ 12a ArbGG)

Keine Kostenerstattung für Anwaltskosten in erster Instanz — im Aktenauszug auf Besonderheit hinweisen.

## Besonderheiten im Aktenauszug

- Stets KSchG-Klagefrist und Zugang der Kündigung prominent darstellen
- Gütetermin als eigenen Verfahrensschritt in der Verfahrenschronologie
- Bei Betriebsratsanhörung (§ 102 BetrVG): Datum und Ordnungsgemäßheit in der Sachverhaltschronologie
- Massenentlassung (§ 17 KSchG): Anzeige bei Agentur für Arbeit als eigenes Ereignis

## Output-Template Kammertermin-Vorbereitung

**Adressat:** Sachbearbeiter — Tonfall: sachlich-juristisch

```
TERMINSVORSCHAU — [AKTENZEICHEN]
Termin: [DATUM] [UHRZEIT] — ArbG [ORT] Saal [X]
Verfahren: [KURZBEZEICHNUNG]
Klagefrist gewahrt: Ja / Nein (§ 4 KSchG — Zugang [DATUM] + 21 Tage = [FRISTENDE])
BR-Anhoerung: Ja / Nein / unklar
Guetetermin: [DATUM] — [ERGEBNIS]
Aktuelle Antraege: 1. Feststellungsklage § 4 KSchG; 2. [...]
Streitige Punkte: [LISTE]
Vergleichsspielraum: [BETRAG] / offenes Zeugnis / beides
```

---
<!-- AUDIT 27.05.2026: Bundle 010 Halluzinations-Reparatur -->

## 2. `fristen-und-terminkalender`

**Fokus:** Anwalt will alle prozessrelevanten Fristen und Termine im Aktenauszug hervorheben: Klagefrist Berufungsfrist Begründungsfrist Verkündungstermin Vollziehungsfrist. Normen §§ 222 517 520 548 ZPO. Prüfraster Vollständigkeit Frist-Berechnung Hervorhebung Fehler-Scan. Output Fristen-Box Fristen-Tabelle. Abgrenzung zu verfahrenschronologie (Prozessschritte) und mittelstand-ma-fristen-cp-kalender (M&A-Fristen).

# Fristen und Terminkalender

## Zweck

Versäumte Fristen können zum Verlust des Verfahrens oder zur Haftung des Rechtsanwalts führen. Dieser Skill identifiziert alle prozessrelevanten Fristen und Termine aus der Akte und stellt sie prominent dar.

## Triage — kläre vor Fristermittlung

1. Wurde das Urteil (erstinstanzlich) bereits zugestellt? (Berufungsfrist läuft!)
2. Liegt ein Hinweisbeschluss des Gerichts mit Frist vor?
3. Wurden Sachverständigenvorschüsse angefordert mit Zahlungsfrist?
4. Handelt es sich um ein Eilverfahren? (Vollziehungsfrist § 929 Abs. 2 ZPO)
5. KSchG-Verfahren? (3-Wochen-Frist § 4 KSchG — absolute Notfrist)

## Zentrale Normen

- § 222 ZPO i.V.m. §§ 187-188 BGB — Fristberechnung (Wochenende, Feiertag)
- § 233-238 ZPO — Wiedereinsetzung in den vorigen Stand bei unverschuldetem Fristversäumnis
- § 517 ZPO — Berufungsfrist 1 Monat; § 520 Abs. 2 ZPO — Begründungsfrist 2 Monate
- § 548 ZPO — Revisionsfrist 1 Monat; § 551 ZPO — Revisionsbegründungsfrist 2 Monate
- § 929 Abs. 2 ZPO — Vollziehungsfrist einstweilige Verfügung 1 Monat
- § 4 KSchG — Klagefrist 3 Wochen (Notfrist); § 74 VwGO — Klagefrist 1 Monat

## Rechtsprechung zu Fristen und Fristversäumnis

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Fristenarten

### Absolute Fristen (gesetzlich, nicht verlängerbar)

| Frist | Norm | Fristdauer | Berechnung |
|---|---|---|---|
| Berufungsfrist | § 517 ZPO | 1 Monat | ab Zustellung Urteil |
| Berufungsbegründungsfrist | § 520 Abs. 2 ZPO | 2 Monate | ab Zustellung Urteil |
| Revisionsfrist | § 548 ZPO | 1 Monat | ab Zustellung Urteil |
| Revisionsbegründungsfrist | § 551 ZPO | 2 Monate | ab Zustellung Urteil |
| Klagefrist KSchG | § 4 KSchG | 3 Wochen | ab Zugang Kündigung |
| Klagefrist VwGO | § 74 VwGO | 1 Monat | ab Zustellung Widerspruchsbescheid |
| Vollziehungsfrist eV | § 929 Abs. 2 ZPO | 1 Monat | ab Zustellung Beschluss |
| Berufungsfrist ArbGG | § 66 ArbGG | 1 Monat | ab Zustellung Urteil |
| Berufungsfrist SGG | § 151 SGG | 1 Monat | ab Zustellung Urteil |

### Richterliche Fristen (verlängerbar)

- Schriftsatzfristen des Gerichts (Klageerwiderung, Replik, Duplik)
- Frist zur Stellungnahme zu Hinweisbeschlüssen
- Frist zur Einzahlung von Auslagen (Sachverständigenvorschuss)

### Notfristen

Fristen, die nicht verlängerbar sind und bei denen Wiedereinsetzung nur unter engen Voraussetzungen möglich ist (z. B. Berufungsfrist).

## Output-Format (Fristenbox am Anfang)

```
FRISTEN UND TERMINE — SOFORT PRUEFEN
Berufungsfrist: TT.MM.JJJJ (§ 517 ZPO)
Begründungsfrist: TT.MM.JJJJ (§ 520 ZPO)
Nächste Verhandlung: TT.MM.JJJJ HH:UU Uhr
Schriftsatzfrist: TT.MM.JJJJ (richterliche Anordnung)
```

Alternativ als Markdown-Tabelle:

```markdown
## Fristen und Termine — Sofort prüfen

| Frist / Termin | Datum | Norm | Status |
|---|---|---|---|
| Berufungsfrist | TT.MM.JJJJ | § 517 ZPO | laeuft |
| Begründungsfrist | TT.MM.JJJJ | § 520 ZPO | laeuft |
| Mündliche Verhandlung | TT.MM.JJJJ | Terminsverfügung | angesetzt |
```

## Berechnungshinweise

- Fristbeginn immer anhand des tatsächlichen Zustellungsdatums aus der Akte ermitteln
- Wenn Zustellungsdatum nicht bekannt: ausdrücklich als "Zustellungsdatum unbekannt — Frist nicht berechenbar" kennzeichnen
- Wochenenden und gesetzliche Feiertage nach § 222 ZPO i.V.m. §§ 187-188 BGB berücksichtigen
- Bei Monatsfristen: Fristende = gleicher Tag des Folgemonats (§ 188 Abs. 2 BGB)

## Qualitätscheck

- [ ] Alle gesetzlichen Fristen aus der Akte erfasst?
- [ ] Fristenbox am Anfang des Aktenauszugs?
- [ ] Berechnungsgrundlage (Zustellungsdatum) angegeben?
- [ ] Fehlende Zustellungsdaten als "unbekannt" markiert?
- [ ] Fristen in der Verfahrenschronologie markiert?
- [ ] Wochenende/Feiertag bei Fristende berücksichtigt (§ 222 ZPO)?

---

## 3. `sozialgerichtsverfahren-modus`

**Fokus:** Aktenauszug für SGG-Verfahren erstellen: Klage Berufung §§ 143 ff. SGG Eilantrag § 86b SGG Widerspruchsverfahren. Amtsermittlungsgrundsatz Sozialversicherungs-Leistungsarten. Normen SGG §§ 51 77 86b 143. Prüfraster SGG-spezifische Fristen Vorverfahrens-Prüfung Leistungsarten. Output SGG-spezifischer Aktenauszug. Abgrenzung zu verwaltungsprozess-modus (VwGO) und arbeitsgerichtsverfahren-modus (ArbGG).

# Sozialgerichtsverfahren-Modus (SGG)

## Zweck

Dieser Modus-Skill aktiviert die verfahrensspezifischen Einstellungen für sozialgerichtliche Verfahren nach dem Sozialgerichtsgesetz (SGG). Sozialgerichtsverfahren betreffen Streitigkeiten im Bereich der Sozialversicherung (GKV, GRV, Arbeitslosenversicherung, Pflegeversicherung, Unfallversicherung) sowie der Grundsicherung.

## Triage — kläre vor Aktivierung des Modus

1. Widerspruch eingelegt? Liegt Widerspruchsbescheid vor? (Klagefrist läuft ab Zustellung!)
2. Eilrechtsschutz erforderlich? (§ 86b SGG — einstweilige Anordnung oder aufschiebende Wirkung)
3. Welches SGB-Kapitel ist betroffen? (SGB II, V, VI, VII, IX, XI, XII)
4. Eigene Beweiserhebung des Gerichts (§ 103 SGG) — wurden Sachverständige oder Aktenbeiziehung angeordnet?

## Zentrale Normen (SGG / SGB)

- § 84 SGG — Widerspruchsfrist 1 Monat ab Bekanntgabe
- § 87 SGG — Klagefrist 1 Monat ab Zustellung Widerspruchsbescheid
- § 86b SGG — Eilrechtsschutz (Abs. 1: aufschiebende Wirkung; Abs. 2: einstweilige Anordnung)
- § 103 SGG — Amtsermittlungsgrundsatz (Untersuchungsgrundsatz)
- § 151 SGG — Berufungsfrist 1 Monat; § 164 SGG — Revisionsfrist 1 Monat
- § 183 SGG — Keine Gerichtskosten für Versicherte (Kostenprivileg)
- § 66 Abs. 2 SGG — Jahresfrist bei fehlerhafter Rechtsbehelfsbelehrung

## Rechtsprechung (BSG / BVerfG — Leitsätze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Sachgebiete der Sozialgerichtsbarkeit

- Krankenversicherung (SGB V)
- Rentenversicherung (SGB VI)
- Unfallversicherung (SGB VII)
- Arbeitsförderung (SGB III)
- Grundsicherung für Arbeitsuchende (SGB II)
- Sozialhilfe (SGB XII)
- Pflegeversicherung (SGB XI)
- Kinder- und Jugendhilfe (SGB VIII)
- Behinderung und Teilhabe (SGB IX)
- Vertragsarztrecht (SGB V, 4. Kapitel)

## Typischer Verfahrensablauf

1. Verwaltungsverfahren beim Leistungsträger
2. Erlass des Ausgangsbescheids
3. Widerspruch (§§ 83 ff. SGG)
4. Widerspruchsbescheid
5. Klage beim Sozialgericht (§ 90 SGG)
6. Berufung beim Landessozialgericht (§§ 143 ff. SGG)
7. Revision beim Bundessozialgericht (§§ 160 ff. SGG)

## Kritische Fristen (SGG)

| Frist | Norm | Dauer | Besonderheit |
|---|---|---|---|
| Widerspruchsfrist | § 84 SGG | 1 Monat | ab Bekanntgabe |
| Klagefrist | § 87 SGG | 1 Monat | ab Zustellung Widerspruchsbescheid |
| Berufungsfrist | § 151 SGG | 1 Monat | ab Zustellung Urteil |
| Revisionsfrist | § 164 SGG | 1 Monat | ab Zustellung Urteil |

**Besonderheit:** Bei fehlender oder fehlerhafter Rechtsbehelfsbelehrung gilt eine Jahresfrist (§ 66 Abs. 2 SGG).

## Eilrechtsschutz (§ 86b SGG)

| Antrag | Ziel | Norm |
|---|---|---|
| Anordnung der aufschiebenden Wirkung | VA hat keine aufschiebende Wirkung | § 86b Abs. 1 SGG |
| Einstweilige Anordnung | Vorläufige Regelung eines Rechtsverhältnisses | § 86b Abs. 2 SGG |

Eilanträge in sozialgerichtlichen Verfahren (z. B. Grundsicherungsleistungen) sind häufig zeitkritisch — im Aktenauszug besonders hervorheben.

## Amtsermittlungsgrundsatz (§ 103 SGG)

Das Sozialgericht ermittelt den Sachverhalt von Amts wegen. Beweisangebote der Parteien sind möglich, aber das Gericht ist nicht daran gebunden. Im Aktenauszug daher:

- Eigene Beweiserhebungen des Gerichts (ärztliche Gutachten, Aktenbeiziehungen) gesondert erfassen
- Beigezogene Behördenakten nennen

## Besonderheiten im Aktenauszug

- Parteibezeichnungen: "Kläger/in" und "Beklagter" (Leistungsträger / Behörde)
- Streitgegenstand ist häufig ein Bescheid über Leistungsgewährung oder -versagung
- Leistungsart und Leistungszeitraum im Verfahrensidentifikationsblock aufführen
- Gutachten (ärztliche / berufskundliche) als eigene Kategorie in Beweismittel-Tabelle
- Kostenrecht: keine Gerichtskosten für Versicherte (§ 183 SGG)
