---
name: unbestimmte-rechtsbegriffe-ungeschriebene
description: "Unbestimmte Rechtsbegriffe Ungeschriebene: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Unbestimmte Rechtsbegriffe Ungeschriebene

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Unbestimmte Rechtsbegriffe Ungeschriebene** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `unbestimmte-rechtsbegriffe-pruefen` | Prüft unbestimmte Rechtsbegriffe: wesentlich, erheblich, zumutbar, geeignet, angemessen, erforderlich. Gibt Auslegungsmassstaeibe aus Rechtsprechung und h.M., Indizien und Fallgruppen. Warnt vor der Grenze mechanischer Subsumtion bei wertungsoffenen Begriffen. |
| `ungeschriebene-merkmale-judikatur` | Identifiziert judicativ entwickelte ungeschriebene Tatbestandsmerkmale: Verkehrspflichten, teleologische Reduktion und Extension, richterrechtliche Fortbildung, Analogie. Warnt vor Grenzen der mechanischen Prüfung bei richterrechtlich gepraegten Normen. |
| `ziel-und-rechtsweg-bestimmung` | Ermittelt interaktiv das Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag, Beschwerde, Strafverfolgung, Verwaltungsakt-Anfechtung) und leitet daraus den einschlaegigen Rechtsweg ab: ZPO, VwGO, SGG, FGO, StPO, FamFG. Warnt bei Zweifelsfaellen. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Unbestimmte Rechtsbegriffe Ungeschriebene**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `unbestimmte-rechtsbegriffe-pruefen`

**Fokus:** Prüft unbestimmte Rechtsbegriffe: wesentlich, erheblich, zumutbar, geeignet, angemessen, erforderlich. Gibt Auslegungsmassstaeibe aus Rechtsprechung und h.M., Indizien und Fallgruppen. Warnt vor der Grenze mechanischer Subsumtion bei wertungsoffenen Begriffen.

# Unbestimmte Rechtsbegriffe prüfen

## Triage zu Beginn — kläre vor der Begriffsprüfung

1. Welcher konkrete unbestimmte Rechtsbegriff ist in welchem Normkontext einschlägig?
2. Liegt ein Beurteilungsspielraum einer Behörde vor? (nur eingeschränkte gerichtliche Kontrolle)
3. Gibt es BGH/BAG/BVerwG-Rechtsprechung zu diesem Begriff in diesem Kontext?
4. Ist der Begriff durch Fallgruppen der Rechtsprechung konkretisiert?
5. Handelt es sich um eine Wertungsfrage, die das System nicht abschließend beantworten kann?

## Zweck

Unbestimmte Rechtsbegriffe sind Tatbestandsmerkmale, deren Inhalt nicht aus dem Wortlaut ablesbar ist und deren Ausfüllung einen normativen Wertungsakt erfordert. Das System nennt Auslegungsmaßstäbe und Indizien — keine abschließende Bewertung.

## Aktuelle Rechtsprechung zur Auslegung unbestimmter Rechtsbegriffe

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wichtige unbestimmte Rechtsbegriffe

### "Wesentlich" / "erheblich"

**Kontext:** § 323 Abs. 5 S. 2 BGB (nicht unerhebliche Pflichtverletzung beim Rücktritt); § 536 BGB (erheblicher Mangel); § 17 Abs. 2 Nr. 1 KSchG.

**Auslegungsmaßstab:** Relation zum Vertragszweck, Schwere der Abweichung.

**Indizien:** Umfang der Abweichung, wirtschaftliche Bedeutung, Behebbarkeit.

### "Zumutbar"

**Kontext:** § 275 Abs. 3 BGB (persönliche Leistungshindernis); § 626 BGB (wichtiger Grund); § 3 AGG; § 5 Abs. 2 ArbSchG.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Entscheidungsbaum:**
```
Welche Interessen stehen auf dem Spiel?
├─ Wirtschaftliche Interessen des Einen vs. Persönlichkeitsrechte des Anderen
│ → Abwägung; Schwere des Eingriffs maßgebend
└─ Beider wirtschaftliche Interessen
 → Verhältnismäßigkeit im engeren Sinne
```

### "Geeignet"

**Kontext:** Verhältnismäßigkeitsprüfung (erstes Mittel); § 1 KSchG.

**Auslegungsmaßstab:** Kausalität im weiteren Sinne — Maßnahme muss den Zweck zumindest fördern können.

### "Angemessen"

**Kontext:** Verhältnismäßigkeit i.e.S.; § 307 BGB (AGB); § 20 Abs. 1 GWB; Art. 6 Abs. 1 lit. f DSGVO.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Indizien bei AGB:** Abweichung vom dispositiven Recht; keine Kompensation; fehlende Transparenz.

### "Erforderlich"

**Kontext:** Verhältnismäßigkeit (Stufe 2); Art. 5 Abs. 1 lit. c DSGVO (Datensparsamkeit).

**Auslegungsmaßstab:** Gibt es ein gleich geeignetes Mittel mit geringerem Eingriff? Vergleich mit realen Alternativen.

### "Wichtiger Grund"

**Kontext:** § 626 BGB (außerordentliche Kündigung); § 543 BGB (Miete); § 314 BGB (Dauerschuldverhältnisse).

**Auslegungsmaßstab:** BGH: Alle Umstände des Einzelfalls; dem Kündigenden ist Festhalten am Vertrag bis Ende nicht zumutbar. Interessenabwägung: Verschulden, Wiederholungsgefahr, Schwere.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Das System nennt:
- Den unbestimmten Rechtsbegriff und den Normkontext
- Den anerkannten Auslegungsmaßstab
- Indizien pro und contra aus dem Nutzersachverhalt
- Ausdrücklicher Hinweis: Das Ergebnis ist eine Indiziensammlung; die abschließende Bewertung obliegt dem Gericht.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

## 2. `ungeschriebene-merkmale-judikatur`

**Fokus:** Identifiziert judicativ entwickelte ungeschriebene Tatbestandsmerkmale: Verkehrspflichten, teleologische Reduktion und Extension, richterrechtliche Fortbildung, Analogie. Warnt vor Grenzen der mechanischen Prüfung bei richterrechtlich gepraegten Normen.

# Ungeschriebene Merkmale und Judikatur

## Zweck

Viele Normen des deutschen Rechts und des Unionsrechts sind durch Rechtsprechung um ungeschriebene Tatbestandsmerkmale ergänzt oder durch teleologische Reduktion eingeschränkt worden. Dieser Skill identifiziert diese judikativ entwickelten Voraussetzungen und integriert sie in die TBM-Liste.

## Was sind ungeschriebene Tatbestandsmerkmale?

Ungeschriebene Merkmale sind Voraussetzungen, die nicht im Gesetzeswortlaut stehen, aber durch ständige Rechtsprechung oder h.M. als konstitutive Bestandteile des Tatbestands anerkannt sind. Sie entstehen durch:

- **Teleologische Reduktion:** Norm ist nach dem Wortlaut einschlägig, wird aber durch die Rechtsprechung auf bestimmte Sachverhalte eingeschränkt (z. B. § 181 BGB: kein Insichgeschäft bei rein rechtlichem Vorteil für den Vertretenen)
- **Teleologische Extension / Analogie:** Norm gilt nach dem Wortlaut nicht, wird aber auf vergleichbare Sachverhalte ausgedehnt (z. B. § 985 BGB analog für bestimmte Situationen)
- **Richterliche Rechtsfortbildung:** Gesamte Rechtsfiguren ohne Normgrundlage (z. B. culpa in contrahendo vor der Kodifizierung in § 311 Abs. 2 BGB; Störung der Geschäftsgrundlage vor § 313 BGB)

## Auslegungsmethoden (§§ 133, 157 BGB)

Die vier klassischen Auslegungsmethoden nach Savigny:

| Methode | Frage | Hilfsmittel |
|---|---|---|
| Grammatisch | Was sagt der Wortlaut? | Wortsinn; Legaldefinitionen; Sprachgebrauch |
| Systematisch | Wie fügt sich die Norm ins Gesetz ein? | Kontext, Überschriften, andere Normen |
| Historisch | Was wollte der Gesetzgeber? | Gesetzgebungsmaterialien (BT-Drucksachen); fachliche Einordnung |
| Teleologisch | Welchem Zweck dient die Norm? | Normzweck; Wertungszusammenhang |

Bei Widerspruch: Teleologische Auslegung hat grundsätzlich Vorrang, wenn der Wortlaut nicht eindeutig ist.

## Wichtige ungeschriebene Merkmale nach Rechtsgebiet

### Deliktsrecht § 823 Abs. 1 BGB

- **Verkehrspflichten:** Wer eine Gefahrenquelle schafft oder beherrscht, muss Dritte davor schützen. Kein Wortlaut in § 823 Abs. 1 BGB — vollständig richterrechtlich entwickelt (BGH-Linie; live zu prüfen unter bgh.de / dejure.org).
- **Verkehrssicherungspflichten:** Inhaber von Anlagen, Grundstücken, Produkten; Haftung für Unterlassen nur bei Garantenstellung.

### Vertragsrecht

- **Nebenpflichten § 241 Abs. 2 BGB:** Rücksicht- und Schutzpflichten; judikativ für jede Vertragsbeziehung entwickelt.
- **Culpa in contrahendo §§ 280 Abs. 1 / 311 Abs. 2 BGB:** Heute kodifiziert; Inhalt weiterhin richterrechtlich geprägt.
- **Wegfall der Geschäftsgrundlage § 313 BGB:** Voraussetzung der "schwerwiegenden Veränderung" ist judikativ ausgefüllt.

### Strafrecht

- **Objektive Zurechnung:** Kein Wortlaut in § 15 StGB; vollständig durch Rechtsprechung entwickelt (Schaffung einer rechtlich missbilligten Gefahr, die sich im Erfolg realisiert).
- **Tatherrschaft (Täterschaft):** § 25 StGB ist ein Rahmen; konkrete Abgrenzung Täter/Teilnehmer ist richterrechtlich geprägt.

### Unionsrecht

- **Effet utile:** Jede Unionsnorm ist so auszulegen, dass ihr praktische Wirksamkeit zukommt (EuGH ständige Rechtsprechung; live unter curia.europa.eu).
- **Staatshaftung für Richtlinienverletzung:** Nicht im AEUV geregelt; durch EuGH Rs. Francovich entwickelt (Rs. C-6/90 und C-9/90; live zu prüfen).

## Teleologische Reduktion — Prüfungsschema

1. Wortlaut der Norm: Ist der Sachverhalt erfasst?
2. Historischer Wille des Gesetzgebers: Sollte dieser Sachverhalt erfasst sein?
3. Telos (Normzweck): Würde die wörtliche Anwendung dem Normzweck widersprechen?
4. Folge: Reduktion des Tatbestands auf Fälle, die dem Normzweck entsprechen.

## Analogie — Prüfungsschema

1. Planwidrige Regelungslücke im Gesetz?
2. Vergleichbarer Sachverhalt (Interessenlage)?
3. Rechtsähnlichkeit (Gleiche Wertungsfrage)?
4. Analoge Anwendung der Norm auf den Sachverhalt.

**Analogieverbot:** Strafrecht (Art. 103 Abs. 2 GG; § 1 StGB); Steuerrecht (Gesetzmäßigkeit der Besteuerung).

## Warnung und Grenzen

Richterrechtlich geprägte Normen können durch das mechanische Prüfsystem nur eingeschränkt erfasst werden. Das System:
- Gibt Hinweise auf bekannte ungeschriebene Merkmale
- Kann nicht ausschließen, dass neuere Entwicklungen der Rechtsprechung nicht erfasst sind
- Empfiehlt bei richterrechtlich geprägten TBM immer eine Live-Recherche (dejure.org, bgh.de) mit aktuellem Datum

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern (dejure.org, bgh.de, curia.europa.eu).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: gesetze-im-internet.de (BGB §§ 133, 157, 181, 241 ff., 311 ff., 313; StGB §§ 1, 15, 25; AEUV); eur-lex.europa.eu (EU-Recht).

## 3. `ziel-und-rechtsweg-bestimmung`

**Fokus:** Ermittelt interaktiv das Nutzerziel (Anspruchsdurchsetzung, Abwehr, Antrag, Beschwerde, Strafverfolgung, Verwaltungsakt-Anfechtung) und leitet daraus den einschlaegigen Rechtsweg ab: ZPO, VwGO, SGG, FGO, StPO, FamFG. Warnt bei Zweifelsfaellen.

# Ziel- und Rechtsweg-Bestimmung

## Triage zu Beginn — kläre vor der Rechtsweg-Bestimmung

1. Was möchte der Nutzer erreichen?
2. Wer ist Gegner? (Privatperson / Unternehmen / Behörde / Staat)
3. Ist Behördenbeteiligung erkennbar? → Öffentliches Recht prüfen
4. Besteht Dringlichkeit? → Eilverfahren parallel skizzieren
5. Wurde ein Vorverfahren (Widerspruch, Einspruch) bereits durchgeführt?

## Zweck

Das Ziel bestimmt den Rechtsweg, die Verfahrensart, die Klageart und letztlich die einschlägigen Normen. Dieser Skill erfasst das Ziel strukturiert und gibt einen ersten Rechtsweg-Hinweis.

## Zentrale Normen zur Rechtswegsbestimmung

- § 13 GVG — ordentliche Gerichtsbarkeit (bürgerliche Rechtsstreitigkeiten)
- § 40 VwGO — Verwaltungsrechtsweg (öffentlich-rechtliche Streitigkeiten)
- § 51 SGG — Sozialgerichtsbarkeit (Sozialversicherung)
- § 33 FGO — Finanzgerichtsbarkeit (Steuern und Abgaben)
- § 2 ArbGG — Arbeitsgerichtsbarkeit (Arbeitsverhältnisse)
- § 17 GVG — Rechtsweg-Verweisung; § 17a GVG — Rüge der Unzuständigkeit

## Zielfragen

**Was möchten Sie erreichen?**

| Nr. | Ziel | Typischer Rechtsweg |
|-----|------|---------------------|
| 1 | Anspruch durchsetzen (Zahlung, Unterlassung, Herausgabe) | ZPO / ordentliche Gerichtsbarkeit |
| 2 | Anspruch abwehren (Klageabweisung, Widerklage) | ZPO |
| 3 | Verwaltungsentscheidung anfechten (Bescheid) | VwGO Anfechtungsklage § 42 Abs. 1 Alt. 1 |
| 4 | Verwaltungsentscheidung erzwingen | VwGO Verpflichtungsklage § 42 Abs. 1 Alt. 2 |
| 5 | Sozialleistung durchsetzen oder anfechten | SGG |
| 6 | Steuerbescheid anfechten | FGO (Einspruch → Klage) |
| 7 | Strafanzeige erstatten | StPO / Staatsanwaltschaft |
| 8 | Verfassungsbeschwerde erheben | BVerfGG § 90 (Erschöpfung Rechtsweg) |
| 9 | Einstweiligen Rechtsschutz | §§ 935/940 ZPO / § 80 Abs. 5 VwGO |
| 10 | Familiensache (Sorge, Unterhalt, Scheidung) | FamFG |
| 11 | Arbeitssache (Kündigung, Lohn) | ArbGG |
| 12 | EU-Recht durchsetzen / anwenden | Nationales Gericht + ggf. Vorabentscheidungsersuchen Art. 267 AEUV |

## Rechtsweg-Entscheidungsbaum

```
Ist eine Behörde beteiligt?
├─ Ja → Handlung hoheitlich?
│ ├─ Ja → VwGO / SGG / FGO (je nach Sachgebiet)
│ │ ├─ Sozialversicherung → SGG
│ │ ├─ Steuer → FGO
│ │ └─ sonst öffentl. Recht → VwGO
│ └─ Nein → ordentliche Gerichtsbarkeit (Fiskusprivileg ausnahmsweise)
└─ Nein → ZPO (ordentliche Gerichtsbarkeit)
 ├─ Schiedsklausel vorhanden? → §§ 1025 ff. ZPO
 ├─ Arbeitssache? → ArbGG
 └─ Familiensache? → FamFG
```

## Vorverfahren und Fristen

| Rechtsweg | Vorverfahren | Frist |
|---|---|---|
| VwGO | Widerspruch (§ 70 VwGO) | 1 Monat ab VA-Bekanntgabe |
| VwGO | Klage nach Widerspruchsbescheid | 1 Monat ab Zustellung WB (§ 74 VwGO) |
| SGG | Widerspruch (§ 83 SGG) | 1 Monat |
| FGO | Einspruch (§ 347 AO) | 1 Monat |
| ArbGG | Kündigungsschutzklage | 3 Wochen ab Zugang Kündigung (§ 4 KSchG) |
| ZPO | keine zwingenden Vorverfahren | Verjährungsfristen (§§ 195 ff. BGB) |

## Zweifelsfälle und Warnungen

- **Doppelte Rechtswegmöglichkeit:** Bei gemischten Sachverhalten (z. B. Amtshaftung § 839 BGB: ordentliche Gerichtsbarkeit; Hoheitsakt: VwGO) ist Trennungsprinzip zu beachten.
- **Rüge der Unzuständigkeit (§ 17a GVG):** Rechtzeitig erheben; Verweisung an zuständiges Gericht möglich.
- **Unionsrecht:** Nationales Gericht wendet EU-Recht an; bei Auslegungsfragen: Vorabentscheidungsersuchen (Art. 267 AEUV; → eu-vorabentscheidung-pruefen).

## Ausgabe

Rechtsweg-Bestimmung mit Entscheidungsbaum, Klageart, Zuständigkeit, Frist und Warnungen bei Zweifelsfällen. Empfehlung zur Folgeskill-Nutzung (z. B. verfahrensart-bestimmen, workflow-fristen-und-risikoampel).

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern (dejure.org, bgh.de, bverfg.de).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: gesetze-im-internet.de (GVG §§ 13, 17, 17a; VwGO §§ 40, 70, 74; SGG § 51; FGO § 33; ArbGG § 2; KSchG § 4; BVerfGG § 90; ZPO §§ 935, 940, 1025 ff.).
