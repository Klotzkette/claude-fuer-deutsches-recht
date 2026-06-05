---
name: eu-vorabentscheidung-falsche-wiese
description: "EU Vorabentscheidung Falsche Wiese: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# EU Vorabentscheidung Falsche Wiese

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **EU Vorabentscheidung Falsche Wiese** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `eu-vorabentscheidung-pruefen` | Prueft die Voraussetzungen des Vorabentscheidungsersuchens nach Art. 267 AEUV: Vorlagebefugnis und -pflicht, CILFIT-Ausnahmen (acte clair/eclaire), Consorzio-Erweiterung, Vorlagepflicht letzter Instanz, Formulierung der Vorlagefrage, curia.europa.eu-Fundstellen. |
| `falsche-wiese-warnung` | Warnt vor typischen Falschverortungen im Recht: Vertrag statt Delikt, Verwaltungsakt vs. Realakt, Strafrecht statt Ordnungswidrigkeit, Unionsrecht statt nationales Recht. Mechanisches Durchprüfen der richtigen Prüfungsebene vor Normanwendung. |
| `fehlerklasse-bgb-at-training` | Ordnet BGB-AT-Fehler in Klausuren: Vertragsschluss, Zugang, Minderjaehrige, Stellvertretung, Anfechtung, Form und Fristen. Trainiert strukturiertes Erkennen, Gewichten und Beheben von Klausurfehlern. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **EU Vorabentscheidung Falsche Wiese**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `eu-vorabentscheidung-pruefen`

**Fokus:** Prueft die Voraussetzungen des Vorabentscheidungsersuchens nach Art. 267 AEUV: Vorlagebefugnis und -pflicht, CILFIT-Ausnahmen (acte clair/eclaire), Consorzio-Erweiterung, Vorlagepflicht letzter Instanz, Formulierung der Vorlagefrage, curia.europa.eu-Fundstellen.

# EU-Vorabentscheidung prüfen (Art. 267 AEUV)

## Zweck

Das Vorabentscheidungsverfahren nach Art. 267 AEUV ermöglicht nationalen Gerichten, dem EuGH Fragen zur Auslegung des Unionsrechts vorzulegen. Dieser Skill prüft, ob die Voraussetzungen eines Vorabentscheidungsersuchens vorliegen, und unterstützt bei der Formulierung der Vorlagefrage.

## Triage zu Beginn

1. Ist die Auslegung von Unionsrecht entscheidungserheblich?
2. Ist das vorlegende Gericht ein "Gericht eines Mitgliedstaats" iSd Art. 267 AEUV?
3. Ist das Gericht letztinstanzlich (Vorlagepflicht) oder fakultativ (Vorlagebefugnis)?
4. Ist eine CILFIT-Ausnahme denkbar (acte clair / acte éclairé)?
5. Ist eine Gültigkeitsfrage involviert (nur EuGH kann Sekundärrecht für ungültig erklären)?

## Voraussetzungen Art. 267 AEUV

### 1. Vorlagebefugnis (Art. 267 Abs. 2 AEUV)

Berechtigt zur Vorlage ist jedes "Gericht eines Mitgliedstaats". Der Begriff ist unionsrechtlich autonom auszulegen; er setzt voraus:
- Gesetzliche Grundlage des Spruchkörpers
- Ständiger Charakter
- Obligatorische Gerichtsbarkeit
- Kontradiktorisches Verfahren
- Anwendung von Rechtsnormen

In Deutschland: alle ordentlichen Gerichte, Verwaltungsgerichte, Finanzgerichte, Sozialgerichte, Arbeitsgerichte. Schiedsgerichte grundsätzlich nicht.

### 2. Vorlagepflicht (Art. 267 Abs. 3 AEUV)

Letztinstanzliche Gerichte (kein Rechtsmittel im nationalen Recht mehr möglich) sind zur Vorlage verpflichtet, wenn die Auslegung des Unionsrechts entscheidungserheblich ist.

In Deutschland: BGH, BVerwG, BAG, BSG, BFH, BVerfG (wenn Unionsrecht berührt).

### 3. Entscheidungserheblichkeit

Die Vorlagefrage muss für den Ausgang des Rechtsstreits erheblich sein. Hypothetische oder rein akademische Fragen sind unzulässig. Zulässig auch bei offensichtlicher Unionsrechtskonformität, wenn das vorlegende Gericht unsicher ist.

### 4. Auslegungsfrage oder Gültigkeitsfrage

Vorlage möglich für:
- Auslegung von Primärrecht (AEUV, EUV, GRCh)
- Auslegung von Sekundärrecht (Verordnungen, Richtlinien, Beschlüsse)
- Gültigkeit von Sekundärrecht (nur EuGH kann Sekundärrecht für ungültig erklären)

**Nicht zulässig:** Vorlage zur Auslegung nationalen Rechts.

## CILFIT-Ausnahmen (Befreiung von der Vorlagepflicht)

Rechtsprechung live prüfen unter curia.europa.eu (Rs. 283/81 — CILFIT; Rs. C-561/19 — Consorzio).

1. **Acte clair:** Die Auslegung ist so offenkundig, dass kein vernünftiger Zweifel verbleibt; das Gericht muss sich vergewissern, dass andere Mitgliedstaaten und der EuGH dieselbe Auffassung teilen würden. Sprachliche Fassungen aller Amtssprachen sind zu berücksichtigen.

2. **Acte éclairé:** Der EuGH hat die betreffende Frage bereits in identischer Konstellation entschieden.

**Consorzio-Erweiterung (2021):** Das letztinstanzliche Gericht ist von der Vorlagepflicht entbunden, wenn es in einem schwebenden Fall eine offensichtlich unhaltbare Auslegung vermeidet und die Nichtvorlageentscheidung begründet.

## Formulierung der Vorlagefrage

Merkmale einer zulässigen und präzisen Vorlagefrage:
- Klar und präzise formuliert
- Auf die Auslegung oder Gültigkeit des Unionsrechts beschränkt
- Kein Verweis auf nationales Recht in der Frage selbst
- Entscheidungserheblichkeit im Vorlagekontext erkennbar

Muster: "Ist Art. X der Verordnung/Richtlinie Y dahin auszulegen, dass [Sachverhaltskonstellation Z] [Rechtsfolge A] auslöst, wenn [Bedingung B]?"

## Verfahrensablauf und Fristen

- Aussetzung des nationalen Verfahrens nach Vorlagebeschluss (§ 148 ZPO analog oder sonderrechtliche Aussetzung)
- Dauer EuGH-Verfahren: ca. 15–24 Monate (Standardverfahren)
- Beschleunigtes Verfahren (Art. 105 VerfO EuGH): bei besonderer Dringlichkeit; Antrag beim EuGH
- Eilvorabentscheidungsverfahren (PPU, Art. 107 VerfO EuGH): bei Freiheitsentzug oder Fragen zu JI-Zusammenarbeit

## Folgen einer Nichtvorlage

Verletzung der Vorlagepflicht kann staatshaftungsrechtliche Konsequenzen haben, wenn dem Einzelnen durch die fehlerhafte Nichtvorlage ein Schaden entsteht (EuGH Rs. C-224/01 — Köbler; live zu prüfen unter curia.europa.eu).

## Ausgabe

Vorlage-Checkliste: Befugnis/Pflicht, Entscheidungserheblichkeit, CILFIT-Ausnahmen, Formulierungsentwurf, Verfahrensfolgen. Empfehlung: Aktuellen Stand in curia.europa.eu prüfen (Suchfunktion nach Artikel und Rechtssachennummer).

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern (curia.europa.eu).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- EU-Normtext live prüfen: eur-lex.europa.eu; Verfahrensordnung EuGH (VerfO) auf curia.europa.eu.

## 2. `falsche-wiese-warnung`

**Fokus:** Warnt vor typischen Falschverortungen im Recht: Vertrag statt Delikt, Verwaltungsakt vs. Realakt, Strafrecht statt Ordnungswidrigkeit, Unionsrecht statt nationales Recht. Mechanisches Durchprüfen der richtigen Prüfungsebene vor Normanwendung.

# Falsche-Wiese-Warnung

## Triage zu Beginn — kläre vor der Normwahl

1. Beschreibe den Sachverhalt in einem Satz: Wer will was von wem woraus?
2. Gibt es eine Willenseinigung (Vertrag) oder eine einseitige Handlung?
3. Ist eine Behörde oder staatliche Stelle beteiligt? → öffentliches Recht prüfen
4. Sind Strafbehörden involviert oder droht eine Strafverfolgung?
5. Hat der Sachverhalt einen EU-Bezug? → Anwendungsvorrang Unionsrecht prüfen

## Zweck

"Auf der falschen Wiese grasen" ist ein klassisches Problem der Rechtsanwendung: Man prüft eine Norm sorgfältig und korrekt — aber die falsche Norm. Dieser Skill kann auf typische Muster hinweisen und Nutzereingaben einer Plausibilitätskontrolle unterziehen.

Dieser Skill wird automatisch oder auf Anforderung aktiviert, wenn der Sachverhalt oder die gewählte Norm Anzeichen einer Fehlverortung enthält.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen zur Einordnung

- § 35 VwVfG — Definition Verwaltungsakt (Regelung, Einzelfall, Außenwirkung)
- § 40 VwGO — Eröffnung des Verwaltungsrechtswegs (öffentlich-rechtliche Streitigkeit)
- § 13 GVG — Eröffnung des ordentlichen Rechtswegs (bürgerliche Rechtsstreitigkeiten)
- § 21 OWiG — Tateinheit von Straftat und Ordnungswidrigkeit (Straftat geht vor)
- Art. 288 AEUV — Unmittelbare Geltung von EU-Verordnungen

## Typische Falschverortungen

### 1. Vertrag statt Delikt (oder umgekehrt)

**Muster:** Nutzer prüft Vertragsrecht (§§ 280 ff. BGB), obwohl kein Vertrag besteht. Oder: Nutzer prüft § 823 Abs. 1 BGB, obwohl eine vertragliche Sonderbeziehung vorliegt.

**Indizien für Fehlverortung:** Keine Willenserklärungen beschrieben; kein Vertragsschluss erwähnt; Handlung ist einseitig schädigend ohne Vertragsbezug.

**Hinweis des Systems:** "Ihr Sachverhalt enthält keinen erkennbaren Vertragsschluss. Bitte prüfen Sie, ob eine deliktische Anspruchsgrundlage (§ 823 Abs. 1 oder Abs. 2 BGB, § 826 BGB) primär einschlägig ist."

### 2. Verwaltungsakt statt Realakt

**Muster:** Nutzer möchte ein staatliches Handeln anfechten, das kein Verwaltungsakt ist (z.B. staatliche Warnung, schlicht-hoheitliches Handeln).

**Indizien:** Kein Regelungscharakter beschrieben; keine Einzelfallentscheidung; keine Rechtsbehelfsbelehrung im Bescheid.

**Entscheidungsbaum:**
```
Hat das staatliche Handeln Regelungscharakter (§ 35 VwVfG)?
├─ Ja → Verwaltungsakt → Anfechtungsklage § 42 VwGO
└─ Nein → Realakt → allg. Leistungsklage/Unterlassungsklage § 40 VwGO
```

### 3. Strafrecht statt Ordnungswidrigkeit (oder umgekehrt)

**Muster:** Nutzer prüft § 303 StGB (Sachbeschädigung), obwohl es sich um eine Ordnungswidrigkeit nach OWiG handeln könnte.

**Hinweis des Systems:** "Prüfen Sie zunächst, ob der Sachverhalt eine Ordnungswidrigkeit nach dem OWiG oder einem Nebengesetz erfüllt. Tateinheit: § 21 OWiG — Strafrecht geht OWiG vor."

### 4. Unionsrecht statt nationales Recht (oder umgekehrt)

**Muster:** Nutzer prüft nationales Datenschutzgesetz (BDSG), obwohl die DSGVO als EU-Verordnung unmittelbar gilt.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 5. Weitere typische Muster

- Schadensersatz statt Unterlassung (und umgekehrt) — § 1004 BGB bei Dauerstörung
- Primäranspruch statt Sekundäranspruch (Erfüllung statt Schadensersatz statt der Leistung)
- WEG-Recht statt BGB-Schuldrecht bei Eigentumswohnungen (WEG seit 01.12.2020 reformiert)
- Erbrecht statt Familienrecht bei Güterstand-Fragen
- Insolvenzrecht als Vorfrage bei Ansprüchen gegen insolvente Schuldner

## Ausgabe

Das System gibt strukturierten Hinweis:
- Erkanntes Muster der Fehlverortung
- Empfohlene Alternativnorm oder -rechtsgebiet
- Frage an den Nutzer: Möchten Sie die alternative Norm prüfen?

Das System setzt die Prüfung der ursprünglich gewählten Norm nur auf ausdrücklichen Nutzerwunsch fort.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `fehlerklasse-bgb-at-training`

**Fokus:** Ordnet BGB-AT-Fehler in Klausuren: Vertragsschluss, Zugang, Minderjaehrige, Stellvertretung, Anfechtung, Form und Fristen. Trainiert strukturiertes Erkennen, Gewichten und Beheben von Klausurfehlern.

# Fehlerklassen im BGB-AT-Training

## Ziel

Dieser Skill führt nicht schematisch durch Fehlerklassen im BGB-AT-Training, sondern zwingt zu einer prüfbaren Arbeitsspur: Sachverhalt, Norm, Tatbestandsmerkmal, Subsumtion, Gegenargument, Beleg und Ergebnis werden getrennt. Er ordnet Fehler nach Schwere und gibt konkrete Korrekturanleitungen.

## Systematik der BGB-AT-Fehlerklassen

### Fehlerklasse 1 — Vertragsschluss (§§ 145–157 BGB)

**Typische Fehler:**
- Angebot und Annahme nicht getrennt geprüft
- Bestimmtheitsgebot des Angebots (Leistung, Preis, Parteien) nicht geprüft
- invitatio ad offerendum (Schaufenster, Katalog, Website) mit Angebot verwechselt
- Zugang der Annahme (§ 130 BGB) übergangen
- Schweigen als Annahme ohne gesetzliche Grundlage akzeptiert (§ 362 HGB als Sonderregel)

**Prüfungsreihenfolge:** Angebot (§ 145) → Erlöschen des Angebots (§§ 146–149) → Annahme (§ 147) → Zugang (§ 130) → Einigung als Ergebnis

### Fehlerklasse 2 — Zugang (§ 130 BGB)

**Typische Fehler:**
- Zugangszeitpunkt bei E-Mail/Fax falsch angesetzt (Geschäftszeit vs. Außerhalb)
- Risikosphäre-Unterschied zwischen Machtbereich und Kenntnisnahme verkannt
- Zugangsvereitelung durch Adressaten (culpa-Theorie) nicht thematisiert

**Merkhilfe:** Zugang = objektive Möglichkeit der Kenntnisnahme unter normalen Umständen.

### Fehlerklasse 3 — Minderjährige (§§ 104–113 BGB)

**Typische Fehler:**
- Altersgrenzen verwechselt (unter 7 Jahre: geschäftsunfähig; 7–17 Jahre: beschränkt geschäftsfähig)
- "lediglich rechtlich vorteilhaft" falsch bewertet (§ 107 BGB)
- Taschengeldparagraph § 110 BGB vergessen (vollständige Mittelverwendung aus eigenen Mitteln)
- Rückwirkende Genehmigung durch gesetzl. Vertreter (§ 108 Abs. 1 BGB) nicht geprüft

### Fehlerklasse 4 — Stellvertretung (§§ 164–181 BGB)

**Typische Fehler:**
- Drei Voraussetzungen der Stellvertretung nicht getrennt: eigene Willenserklärung + Offenkundigkeitsprinzip (§ 164 Abs. 1) + Vertretungsmacht
- Arten der Vertretungsmacht nicht unterschieden: Vollmacht (§ 166), gesetzliche (§§ 1626, 1793 BGB), organschaftliche
- Rechtsscheinvollmacht (Duldungs- und Anscheinsvollmacht) ohne BGH-Prüfschema
- Insichgeschäft § 181 BGB: Ausnahme "lediglich rechtlich vorteilhaft" übersehen

### Fehlerklasse 5 — Anfechtung (§§ 119–124 BGB)

**Typische Fehler:**
- Anfechtungsgrund vor Anfechtungserklärung prüfen (systematisch verkehrt)
- Anfechtungsfristen: § 121 BGB (unverzüglich bei §§ 119–120); § 124 BGB (Jahresfrist bei Täuschung/Drohung)
- Wirkung ex tunc (§ 142 Abs. 1 BGB) vs. Rechtsfolgen des § 122 BGB (Vertrauensschaden)
- Motivirrtum mit Inhalts- oder Erklärungsirrtum verwechselt (§ 119 Abs. 1 BGB)

### Fehlerklasse 6 — Formvorschriften (§§ 125, 126 ff. BGB)

**Typische Fehler:**
- Rechtsfolge der Formverletzung nicht benannt (§ 125 S. 1 BGB: Nichtigkeit)
- Heilungsvorschriften übergangen (§ 311b Abs. 1 S. 2 BGB: Auflassung und Eintragung heilen formlosen Kaufvertrag über Grundstück)
- Textform (§ 126b BGB) mit Schriftform (§ 126 BGB) verwechselt

### Fehlerklasse 7 — Prüfungsreihenfolge und Normenkonkurrenz

**Typische Fehler:**
- BGB AT vor BGB BT prüfen (zuerst Vertragsschluss, dann Mängelrechte etc.)
- Primäranspruch vor Sekundäranspruch (erst Erfüllung § 433, dann Schadensersatz §§ 280 ff.)
- Vertrag vor Delikt (§§ 280 ff. vor § 823 BGB)
- Spezialgesetz (z. B. CISG, UmwG) vor BGB nicht geprüft

## Red-Team-Fragen

- Welche Anspruchsgrundlage oder Norm ist verführerisch, aber falsch?
- Welche Tatsache wird im Sachverhalt nur behauptet, aber nicht belegt?
- Welche Rechtsfolge passt nicht zur gewählten Norm?
- Wo droht eine falsche Reihenfolge?
- Ist die gewählte Norm im aktuellen Fassungsstand zu prüfen? (gesetze-im-internet.de)

## Bewertungsraster

| Fehlertyp | Schwere | Heilung |
|---|---|---|
| Fehlende Norm | Hoch | Richtige Norm einsetzen, Vier-Schritt wiederholen |
| Fehlende Definition | Mittel | Definition mit Quelle ergänzen |
| Sprung-Subsumtion | Mittel | Tatsachen unter Definition subsumieren |
| Zirkelschluss | Hoch | Definition aus externer Quelle; Tatsachen separat |
| Falsche Reihenfolge | Mittel–Hoch | Prüfungsplan korrigieren |

## Ausgabe

Korrekturvermerk, Randbemerkungen, Punkteindikation und verbesserte Musterpassage. Nenne Rechtsprechung nur, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle live vorliegen (dejure.org, bgh.de); keine Blindzitate.

## Quellenregel

- Normtext live prüfen: gesetze-im-internet.de (BGB in aktuellem Fassungsstand).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle (dejure.org, openjur.de, bgh.de).
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
