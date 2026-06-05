---
name: rechtsfolge-bestimmen-einreden-interaktiver
description: "Rechtsfolge Bestimmen Einreden Interaktiver: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Rechtsfolge Bestimmen Einreden Interaktiver

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Rechtsfolge Bestimmen Einreden Interaktiver** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `rechtsfolge-bestimmen` | Bestimmt die Rechtsfolge nach erfolgreicher Subsumtion: Anspruchsinhalt, Hoehe, Tenor, Verwaltungsakt-Inhalt, Strafmass-Rahmen. Unterscheidet Primaeranspruch, Sekundaeranspruch und Nebenansprüche. Gibt Berechnungshinweise für Schadensersatz und Vertragsstrafen. |
| `spezial-einreden-compliance-dokumentation-und-akte` | Einreden: Compliance-Dokumentation und Aktenvermerk im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-interaktiver-erstpruefung-und-mandatsziel` | Interaktiver: Erstprüfung, Rollenklärung und Mandatsziel im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Rechtsfolge Bestimmen Einreden Interaktiver**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `rechtsfolge-bestimmen`

**Fokus:** Bestimmt die Rechtsfolge nach erfolgreicher Subsumtion: Anspruchsinhalt, Hoehe, Tenor, Verwaltungsakt-Inhalt, Strafmass-Rahmen. Unterscheidet Primaeranspruch, Sekundaeranspruch und Nebenansprüche. Gibt Berechnungshinweise für Schadensersatz und Vertragsstrafen.

# Rechtsfolge bestimmen

## Triage zu Beginn — kläre vor der Rechtsfolgenbestimmung

1. Ist der Tatbestand vollständig positiv subsumiert und sind Einwendungen/Einreden geprüft?
2. Handelt es sich um Primäranspruch (Erfüllung) oder Sekundäranspruch (Schadensersatz)?
3. Sind Nebenansprüche (Verzugszinsen, Anwaltskosten, Kosten) geltend zu machen?
4. Ist der Schaden berechenbar oder wird Schätzung nach § 287 ZPO erforderlich?
5. Ist die Rechtsfolge vollstreckungsfähig? (Tenor bestimmt genug für Vollstreckung)

## Zweck

Ist der Tatbestand erfüllt und sind Einwendungen und Einreden geprüft, bestimmt dieser Skill die konkrete Rechtsfolge.

## Zentrale Normen

- § 249 BGB — Naturalrestitution als Grundform des Schadensersatzes
- § 249 Abs. 2 BGB — Geldersatz bei Körperverletzung/Sachbeschädigung
- § 252 BGB — Entgangener Gewinn
- § 253 Abs. 2 BGB — Schmerzensgeld (immaterieller Schaden)
- § 288 BGB — Verzugszinsen (5 Prozentpunkte über Basiszinssatz; B2B: 9 Prozentpunkte)
- § 339 BGB — Vertragsstrafe; § 343 BGB — richterliche Herabsetzung
- §§ 704 ff. ZPO — Vollstreckungsvoraussetzungen (Titel, Klausel, Zustellung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Kategorien von Rechtsfolgen

### Zivilrecht — Erfüllungsansprüche (Primär)

- Zahlung einer bestimmten Geldsumme (Hauptforderung)
- Herausgabe einer Sache (§ 985 BGB)
- Unterlassung einer Handlung (§ 1004 BGB; §§ 8 ff. UWG)
- Beseitigung einer Beeinträchtigung
- Vornahme einer Handlung (Leistungsurteil nach § 894 ZPO)

### Zivilrecht — Schadensersatz (Sekundär)

**Grundregel:** Naturalrestitution (§ 249 Abs. 1 BGB) — Herstellung des Zustands ohne das schädigende Ereignis.

**Schadensberechnung:**
- Differenzhypothese: Vergleich hypothetischer Zustand ohne Ereignis vs. tatsächlicher Zustand
- Entgangener Gewinn (§ 252 BGB): Wahrscheinlichkeit nach gewöhnlichem Verlauf
- Schmerzensgeld (§ 253 Abs. 2 BGB): nur bei Körper-, Gesundheits-, Freiheits- oder sexueller Selbstbestimmungsverletzung; Bemessung nach Schwere der Verletzung, Dauer der Beeinträchtigung und Verschuldensgrad

### Vertragsstrafe

§ 339 BGB: Verwirkung bei Pflichtverletzung; Höhe nach Vereinbarung. Das System prüft:
- Vertragsstrafe vereinbart?
- Verwirkt (Pflichtverletzung nachgewiesen)?
- Nach § 343 BGB herabzusetzen? (richterliche Herabsetzung bei grobem Missverhältnis zum tatsächlichen Schaden)

### Nebenansprüche

- Verzugszinsen § 288 BGB: 5 Prozentpunkte über Basiszinssatz (Verbraucher); 9 Prozentpunkte über Basiszinssatz (B2B)
- Prozesskosten (§ 91 ZPO): Unterlieger trägt; Berechnung nach GKG und RVG
- Rechtsanwaltskosten als Verzugsschaden: bei Beauftragung eines Anwalts nach Verzugseintritt (§§ 280/286 BGB)

### Verwaltungsrecht — Verwaltungsakt-Inhalt

Das System beschreibt den Tenor eines Verwaltungsakts:
- Belastender VA (Gebot, Verbot, Nebenbestimmungen): Prüfung von Bestimmtheit § 37 VwVfG und Verhältnismäßigkeit
- Begünstigender VA (Genehmigung, Zulassung): Prüfung von Auflagen und Bedingungen

### Strafrecht — Strafrahmen

Das System nennt den gesetzlichen Strafrahmen (Mindest- und Höchststrafe nach StGB) und weist auf strafzumessungsrelevante Umstände hin (§ 46 StGB). Es gibt keine Prognose für das konkrete Strafmaß.

## Entscheidungsbaum Rechtsfolge

```
Tatbestand erfüllt → Rechtsfolge bestimmen
├─ Primäranspruch (Erfüllung): § 433/280 BGB → Zahlung / Herausgabe / Unterlassung
│ └─ Noch nicht erfüllt? → Klage auf Erfüllung
├─ Sekundäranspruch (SE): § 249 BGB → Naturalrestitution
│ ├─ Körperverletzung/Sachbeschädigung? → § 249 Abs. 2 BGB Geldersatz möglich
│ └─ Immaterielle Schäden? → § 253 Abs. 2 BGB Schmerzensgeld
└─ Nebenansprüche: Verzugszinsen § 288 BGB + RK als SE
```

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `spezial-einreden-compliance-dokumentation-und-akte`

**Fokus:** Einreden: Compliance-Dokumentation und Aktenvermerk im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Einreden: Compliance-Dokumentation und Aktenvermerk

## Aufgabe

Dieser Skill strukturiert die Arbeit an Einreden und Einwendungen im Subsumtions-und sichert gleichzeitig die Compliance-Dokumentation. Ergebnis ist ein sofort nutzbarer Aktenvermerk, der Einreden belegt, Risiken bewertet und den nächsten Schritt benennt.

## Systematik: Einreden und Einwendungen

### Einwendungen (wirken von Amts wegen)
- Fehlender Tatbestand (Primärprüfung)
- Nichtigkeitsgründe: §§ 125, 134, 138, 142 BGB (Form, Verstoß gegen Verbotsgesetz, Sittenwidrigkeit, Anfechtung)
- Verjährung ist Einrede, nicht Einwendung (§ 214 BGB); Gericht prüft nicht von Amts wegen

### Einreden (nur auf Erhebung hin wirksam)
- Verjährung §§ 194 ff. BGB; regelmäßige Frist 3 Jahre (§ 195 BGB); Beginn § 199 BGB
- Zurückbehaltungsrecht § 273 BGB (Gegenanspruch aus demselben rechtlichen Verhältnis)
- Zurückbehaltungsrecht § 320 BGB (gegenseitiger Vertrag; Erfüllung Zug-um-Zug)
- Aufrechnung §§ 387 ff. BGB (Gegenforderung fällig, gleichartig, durchsetzbar)

### Einreden aus besonderem Rechtsverhältnis
- § 242 BGB (Treu und Glauben): venire contra factum proprium, Verwirkung, unzulässige Rechtsausübung
- § 438 BGB: Verjährung kaufrechtlicher Mängelansprüche (2 Jahre ab Ablieferung; 5 Jahre bei Bauwerken)
- § 634a BGB: Verjährung werkvertraglicher Mängelansprüche
- § 548 BGB: Verjährung mietrechtlicher Ansprüche (6 Monate)
- § 852 BGB: Deliktsrechtliche Verjährung mit bereicherungsrechtlicher Nachwirkung

## Compliance-Dokumentation im Aktenvermerk

### Mindestinhalt Aktenvermerk zu Einreden

1. **Datum der Mandatsübernahme und erkannte Einreden**
2. **Verjährungsfrist und Fristbeginn** (mit Berechnungsschema und Quelle)
3. **Fristhemmung** (§§ 203–213 BGB) — Verhandlungen, Rechtsverfolgung, höhere Gewalt
4. **Empfehlung zur Klageerhebung oder Fristverlängerung** (z. B. Anerkenntnisunterbrechung, Klagerhebung)
5. **Beweisangebote der Gegenseite zur Einrede** (wer beweist was?)
6. **Risikoampel:** Ist die Einrede erhoben? Belegt? Streitig?

### Musterstruktur Aktenvermerk

```
Datum: TT.MM.JJJJ
Aktenzeichen: ...
Sachverhalt: kurze Zusammenfassung (max. 5 Sätze)
Einreden:
 1. Verjährung: Fristbeginn ..., Ablauf ..., Hemmung vorhanden/nicht vorhanden (Quelle: ...)
 2. § 273 BGB: Gegenanspruch ..., Fälligkeit ..., belegt durch ...
Risikoampel: Rot / Gelb / Grün
Handlung: [Sofortmaßnahme mit Frist und Zuständigkeit]
```

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow

1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Einreden-Normen prüfen (BGB, ggf. HGB, ZPO-Einreden wie § 796 ZPO).
3. **Prüfpunkte abarbeiten:** Welche Einreden sind schlüssig erhoben? Welche fehlen noch? Beweislage?
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen (z. B. workflow-fristen-und-risikoampel, spezial-rechtsfolgen-zahlen-schwellen-und-berechnung).

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** Aktenvermerk oder Schriftsatzbaustein zu Einreden.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel

- Aktuelle Normen live prüfen: gesetze-im-internet.de (BGB §§ 194 ff., 273, 320, 387 ff., 438 etc.).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle (dejure.org, bgh.de).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn der Nutzer den Volltext bereitstellt.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `spezial-interaktiver-erstpruefung-und-mandatsziel`

**Fokus:** Interaktiver: Erstprüfung, Rollenklärung und Mandatsziel im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Interaktiv: Erstprüfung, Rollenklärung und Mandatsziel

## Aufgabe

Dieser Skill führt die interaktive Erstprüfung durch. Er klärt Rolle, Mandatsziel und Sachverhalt, bevor die eigentliche Subsumtion beginnt. Ergebnis ist ein klares Fallbild, das alle weiteren Skills im Plugin gezielt ansteuern lässt.

## Warum Erstprüfung zuerst?

Ohne Rollenklärung und Mandatsziel riskiert die Subsumtion:
- Prüfung der falschen Norm (z. B. Kläger-Perspektive statt Beklagter)
- Übersehen von Fristen oder Verfahrenshindernissen
- Unnötige Prüftiefe bei aussichtslosen Ansprüchen
- Falschen Output (Memo statt Schriftsatz; Klausurstil statt Mandantenbrief)

## Rollenklärung

### Mögliche Rollen der fragenden Person

| Rolle | Konsequenz für die Prüfung |
|---|---|
| Kläger / Anspruchsteller | Anspruchsgrundlage, Beweislast für anspruchsbegründende TBM |
| Beklagter / Anspruchsgegner | Einreden, Einwendungen, Beweislastumkehr-Check |
| Anwalt (beratend) | Erfolgsaussichten, Kostenrisiko, strategische Optionen |
| Anwalt (Schriftsatz) | Klage, Klageerwiderung, Berufungsbegründung |
| Richter / Rechtspfleger | Neutrale Prüfung; Entscheidungsreife; Hinweispflicht § 139 ZPO |
| Klausurkandidat | Gutachtenstil; Fehlerklassen; Bewertungsmaßstab |
| Behördenmitarbeiter | Verwaltungsverfahren; VA-Prüfung; Widerspruchsverfahren |

## Mandatsziel klären

**Mögliche Ziele:**

1. Anspruch durchsetzen (Zahlung, Unterlassung, Herausgabe, Feststellung)
2. Anspruch abwehren (Klageabweisung, Widerklage, Einreden erheben)
3. Verwaltungsentscheidung anfechten (Widerspruch, Anfechtungsklage VwGO)
4. Vorläufigen Rechtsschutz sichern (einstweilige Verfügung §§ 935/940 ZPO; § 80 Abs. 5 VwGO)
5. Gutachten oder Klausurkorrektur erstellen
6. Mandanteninformation (Alltagssprache)
7. Internationalen Sachverhalt mit IPR-Bezug prüfen

## Fünf Kernfragen zur Erstprüfung

1. **Wer fragt?** Rolle und Gegenüber benennen.
2. **Was ist das Ziel?** Anspruch, Abwehr, Gutachten, Schriftsatz, Information?
3. **Was ist die kritische Frist?** Verjährung, Ausschluss, Klagefrist, Widerspruchsfrist?
4. **Was liegt vor?** Unterlagen, Belege, Bescheide, Verträge — Kurzinventar.
5. **Was ist der gewünschte Output?** Memo, Schriftsatz, Checkliste, Brief, Tabelle?

## Erstprüfungs-Fallbild

Das System erstellt nach Klärung der fünf Fragen ein Fallbild:

```
Rolle: [Kläger / Beklagter / Anwalt / Klausurkandidat / ...]
Ziel: [Anspruch X gegen Y aus Norm Z]
Frist: [Verjährung TT.MM.JJJJ / Klagefrist TT.MM.JJJJ / keine erkennbare]
Unterlagen: [vorhanden: Vertrag, Rechnung; fehlend: Zustellungsnachweis]
Output: [Klageschrift / Memo / Mandantenbrief / Klausurgutachten]
Nächster Skill: [→ darlegungs-und-beweislast-verteilen / workflow-fristen-und-risikoampel / ...]
```

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow

1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen und begründen.

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel

- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle (dejure.org, bgh.de, bverfg.de, curia.europa.eu).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn der Nutzer den Volltext bereitstellt.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
