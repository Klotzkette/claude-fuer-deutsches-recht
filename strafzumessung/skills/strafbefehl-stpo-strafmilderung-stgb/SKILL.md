---
name: strafbefehl-stpo-strafmilderung-stgb
description: "Strafbefehl Stpo Strafmilderung Stgb: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Strafbefehl Stpo Strafmilderung Stgb

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Strafbefehl Stpo Strafmilderung Stgb** im Plugin Strafzumessung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `strafbefehl-strafzumessung-407-stpo` | Strafzumessung im Strafbefehl § 407 StPO. Strafrahmen Strafbefehl bis 360 Tagessaetze Geldstrafe; Freiheitsstrafe bis 1 Jahr nur mit Bewaehrung und nur bei Pflichtverteidiger. Pauschalisierung der Strafzumessung. Tagessatzhoehe oft schaetzungsweise. Verteidigungs-Strategie bei zu hoher Strafe: Einspruch oder beschraenkter Einspruch § 410 Abs. 2 StPO. |
| `strafmilderung-49-stgb-zwingend-fakultativ` | Strafmilderung nach § 49 StGB. Abs. 1 zwingende Milderung mit konkreten Bezugsgroessen Hoechstmass 3/4 Mindeststrafe ermaessigt; bei lebenslang 3 bis 15 Jahre. Abs. 2 fakultative Milderung bis zum gesetzlichen Mindestmass. Anwendungsfaelle Versuch § 23 Abs. 2, Beihilfe § 27 Abs. 2, persoenliche Merkmale § 28 Abs. 1, verminderte Schuldfaehigkeit § 21, Verbotsirrtum § 17, TOA § 46a. Mehrfachmilderung. |
| `strafrahmen-und-strafzumessungsstufen` | Strafrahmen-Logik vor der konkreten Zumessung. Aufbau abstrakter Strafrahmen aus Grundtatbestand, Qualifikation, Privilegierung. Modifikationen durch Regelbeispiele und minder schweren Fall. Verschiebung durch §§ 49 Abs. 1 23 Abs. 2 28 Abs. 1 StGB. Aufbau konkreter Strafrahmen, Ableitung der konkreten Strafe nach § 46 StGB. Schnittstelle Strafmilderung und Strafzumessung. |

## Arbeitsweg

Im Plugin Strafzumessung gilt für **Strafbefehl Stpo Strafmilderung Stgb**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `strafbefehl-strafzumessung-407-stpo`

**Fokus:** Strafzumessung im Strafbefehl § 407 StPO. Strafrahmen Strafbefehl bis 360 Tagessaetze Geldstrafe; Freiheitsstrafe bis 1 Jahr nur mit Bewaehrung und nur bei Pflichtverteidiger. Pauschalisierung der Strafzumessung. Tagessatzhoehe oft schaetzungsweise. Verteidigungs-Strategie bei zu hoher Strafe: Einspruch oder beschraenkter Einspruch § 410 Abs. 2 StPO.

# Strafzumessung im Strafbefehlsverfahren — § 407 StPO

## Worum geht es?

Der Strafbefehl ist ein **schriftliches** Verfahren ohne Hauptverhandlung. Die Strafzumessung erfolgt **pauschalisiert** anhand der Akte. § 407 Abs. 2 StPO begrenzt den Sanktionskatalog: Geldstrafe bis 360 Tagessaetze, Fahrverbot, Einziehung, in Ausnahmefaellen Freiheitsstrafe bis 1 Jahr mit Bewaehrung (und Pflichtverteidigung). Verteidigungssicht: bei zu hoher Strafe Einspruch oder beschraenkter Einspruch nach § 410 Abs. 2 StPO.

## Wann brauchen Sie diese Skill?

- Mandant hat einen Strafbefehl erhalten und Sie pruefen die Strafzumessung.
- Sie ueberlegen, ob ein beschraenkter Einspruch auf Rechtsfolgen sinnvoll ist.
- Sie pruefen die Tagessatzfestsetzung gegen den Mandanteneinkommensstand.

## Rechtliche Grundlagen

- **§ 407 Abs. 1 StPO** — Strafbefehl auf Antrag der Staatsanwaltschaft bei Vergehen.
- **§ 407 Abs. 2 StPO** — Sanktionskatalog:
 - Nr. 1: Geldstrafe, Verwarnung mit Strafvorbehalt, Fahrverbot, Entziehung der Fahrerlaubnis, Sperre fuer Fahrerlaubniserteilung, Einziehung, Vernichtung, Unbrauchbarmachung, Bekanntmachung, Geldbusse.
 - Nr. 2: Freiheitsstrafe bis 1 Jahr **mit Bewaehrung und nur mit Verteidiger**.
- **§ 408 StPO** — Erlass durch Richter; Pruefung des hinreichenden Tatverdachts.
- **§ 410 Abs. 1 StPO** — Einspruchsfrist 2 Wochen ab Zustellung.
- **§ 410 Abs. 2 StPO** — Beschraenkung des Einspruchs auf Rechtsfolgen; Schuldspruch wird rechtskraeftig.
- **§§ 40-43 StGB** — Geldstrafe.
- **§ 46 StGB** — Strafzumessungsgrundsatz.

## Strafzumessungs-Grundsatz

Im Strafbefehlsverfahren wird die Strafzumessung haeufig **pauschal** vorgenommen:

- Die Tatumstaende ergeben sich allein aus der Akte.
- Persoenliche und wirtschaftliche Verhaeltnisse werden oft geschaetzt (§ 40 Abs. 3 StGB).
- Strafzumessungstatsachen nach § 46 Abs. 2 StGB werden gewuerdigt, aber ohne Anhoerung des Beschuldigten.

## Schritt-fuer-Schritt-Anleitung (Verteidigung)

1. **Strafbefehl pruefen**:
 - Welche Tatbestaende, welcher Strafrahmen?
 - Welche Anzahl Tagessaetze? Welcher Tagessatz?
 - Gibt es Fahrverbot, Einziehung, Nebenfolgen?
2. **Strafzumessung pruefen**:
 - **Tagessatzanzahl**: Ist die Schuldkomponente realistisch? Vgl. `geldstrafe-tagessatzanzahl-bestimmen`.
 - **Tagessatzhoehe**: Stimmt die Einkommensschaetzung? Vgl. `tagessatzhoehe-40-ii-stgb-nettotagesverdienst`.
 - **§ 47 StGB**: Wenn Freiheitsstrafe verhaengt, sind die "besonderen Umstaende" begruendet?
3. **Beschraenkter Einspruch** (§ 410 Abs. 2 StPO): Schuldspruch wird rechtskraeftig; nur Rechtsfolgen werden in der Hauptverhandlung verhandelt. **Vorsicht**: BZRG-Eintrag bleibt; berufsrechtliche Folgen pruefen.
4. **Unbeschraenkter Einspruch**: Schuldspruch wird mitverhandelt; auch Freispruch moeglich.
5. **Strafmilderungsangebote** vorbereiten:
 - TOA / Schadenswiedergutmachung (§ 46a StGB).
 - Einkommensnachweise fuer realistische Tagessatzhoehe.
 - Gestaendnis bei Einspruchsverhandlung (Gestaendnis-Rabatt).

## Tagessatzhoehe — typische Korrektur-Hebel

- Gericht schaetzt oft optimistisch.
- Einkommensnachweise (Lohnabrechnung letzte 3 Monate; Steuerbescheid; BWA bei Selbststaendigen).
- Unterhaltspflichten substantiiert vortragen.
- Konsumschulden nur ausnahmsweise.

## Strafbefehl mit Freiheitsstrafe bis 1 Jahr (§ 407 Abs. 2 Nr. 2 StPO)

- Nur **mit** Verteidiger und nur **mit** Bewaehrung.
- Voraussetzungen Bewaehrung (§ 56 StGB): Sozialprognose positiv.
- Wenn Sozialprognose fragwuerdig: **Einspruch zwingend**, sonst rechtskraeftige Verurteilung.

## Beschraenkter Einspruch — strategische Pruefung

| Vorteil | Nachteil |
|---|---|
| Schnelle Erledigung | BZRG-Eintrag bleibt |
| Nur Rechtsfolgen-Verhandlung | Schuldspruch rechtskraeftig |
| Kosten geringer | Berufsrechtliche Folgen |
| Geringere Strafverschaerfungsgefahr | Spaetere Strafzumessung beruecksichtigt Vorstrafe |

## Verteidigungs-Argumentationsmuster fuer Einspruch

- "Die Tagessatzhoehe von [X] EUR ist nicht zutreffend, da das Nettoeinkommen meines Mandanten [...] betraegt; Beleg: [...]."
- "Eine Geldstrafe von [X] Tagessaetzen wird der Schuld nicht gerecht; Strafmilderungsgruende [...] sind unberuecksichtigt geblieben."
- "§ 46a StGB ist anwendbar, da [Beleg fuer TOA / Wiedergutmachung]."

## Typische Fehler

- **Einspruchsfrist verpennt** (2 Wochen, § 410 StPO).
- **Beschraenkter Einspruch** ohne BZRG-Pruefung gewaehlt — Folgewirkungen unterschaetzt.
- **Tagessatzhoehe** akzeptiert ohne Einkommensnachweise.
- **Strafmilderungsgruende** in der Strafbefehlspruefung uebersehen.
- **Freiheitsstrafe ohne Verteidiger** im Strafbefehl: Anhaltspunkt fuer Pflichtverteidigung pruefen (§ 140 StPO).

## Querverweise

- `orientierung-strafzumessung-triage` — Eingang ins Plugin.
- `geldstrafe-tagessatzanzahl-bestimmen` — Anzahl.
- `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` — Hoehe.
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Vorrang Geldstrafe.
- Plugin `strafbefehl-verteidiger` — Gesamtverteidigung gegen Strafbefehl.

## Quellen und Stand 05/2026

- §§ 407-412 StPO in der geltenden Fassung.
- §§ 40-43, 46, 47, 56 StGB.
- Quellenregel: vgl. `references/zitierweise.md`.

## 2. `strafmilderung-49-stgb-zwingend-fakultativ`

**Fokus:** Strafmilderung nach § 49 StGB. Abs. 1 zwingende Milderung mit konkreten Bezugsgroessen Hoechstmass 3/4 Mindeststrafe ermaessigt; bei lebenslang 3 bis 15 Jahre. Abs. 2 fakultative Milderung bis zum gesetzlichen Mindestmass. Anwendungsfaelle Versuch § 23 Abs. 2, Beihilfe § 27 Abs. 2, persoenliche Merkmale § 28 Abs. 1, verminderte Schuldfaehigkeit § 21, Verbotsirrtum § 17, TOA § 46a. Mehrfachmilderung.

# Strafmilderung — § 49 StGB

## Worum geht es?

§ 49 StGB enthaelt die **technische** Anleitung, wie der Strafrahmen verschoben wird, wenn das Gesetz auf die Milderung verweist. **Abs. 1** ist eine **zwingende** Milderung mit konkret bestimmten Bezugsgroessen. **Abs. 2** ist eine **fakultative** Milderung; sie laesst es zu, die Strafe bis zum gesetzlichen Mindestmass abzusenken oder statt Freiheitsstrafe auf Geldstrafe zu erkennen.

## Wann brauchen Sie diese Skill?

- Sie pruefen, ob ein Tatbestandsmerkmal oder eine Strafrechtsfigur § 49 StGB ausloest (Versuch, Beihilfe, § 28 Abs. 1 StGB, § 21 StGB, § 17 StGB, § 46a StGB).
- Sie bestimmen den konkreten Strafrahmen vor der eigentlichen Zumessung.
- Sie pruefen ein Urteil revisionsmaessig auf richtige Anwendung des § 49 StGB.

## Rechtliche Grundlagen

### § 49 Abs. 1 StGB — Zwingende Milderung

Wenn das Gesetz die Milderung nach dieser Vorschrift vorschreibt:

- **Nr. 1**: Statt **lebenslanger** Freiheitsstrafe Freiheitsstrafe **3 bis 15 Jahre**.
- **Nr. 2**: Bei zeitiger Freiheitsstrafe darf hoechstens **3/4** des angedrohten Hoechstmasses verhaengt werden.
- **Nr. 3**: Das erhoehte Mindestmass einer Freiheitsstrafe ermaessigt sich:
 - bei einem Mindestmass von 10 oder 5 Jahren auf 2 Jahre;
 - bei einem Mindestmass von 3 oder 2 Jahren auf 6 Monate;
 - bei einem Mindestmass von 1 Jahr auf 3 Monate;
 - im uebrigen auf das gesetzliche Mindestmass.

### § 49 Abs. 2 StGB — Fakultative Milderung

Das Gericht kann nach pflichtgemaessem Ermessen die Strafe **bis zum gesetzlichen Mindestmass der angedrohten Strafart mildern** oder statt Freiheitsstrafe auf **Geldstrafe** erkennen.

## Anwendungsfaelle § 49 Abs. 1 StGB (zwingend)

- **§ 23 Abs. 2 StGB** — Versuch (kann gemildert werden); wenn das Gericht milden moechte, milderts nach § 49 Abs. 1 StGB. (Bei Versuch ist die Milderung selbst fakultativ, aber wenn gemildert, dann nach Abs. 1.)
- **§ 27 Abs. 2 StGB** — Beihilfe: Strafe ist **zwingend** nach § 49 Abs. 1 StGB zu mildern.
- **§ 28 Abs. 1 StGB** — Bei fehlenden strafbegruendenden persoenlichen Merkmalen des Teilnehmers Milderung nach § 49 Abs. 1 StGB.
- **§ 17 Satz 2 StGB** — Vermeidbarer Verbotsirrtum: Milderung **kann** nach § 49 Abs. 1 StGB erfolgen.
- **§ 21 StGB** — Verminderte Schuldfaehigkeit: Milderung **kann** nach § 49 Abs. 1 StGB.
- **§ 46a StGB** — TOA oder Schadenswiedergutmachung: Strafmilderung nach § 49 Abs. 1 StGB **oder** bei Strafe nicht ueber 1 Jahr **Absehen von Strafe**; vgl. `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung`.
- **§ 46b StGB** — Aufklaerungshilfe (Kronzeugenregelung): kann nach § 49 Abs. 1 StGB gemildert oder bei Mindeststrafe unter 3 Jahren Absehen von Strafe.
- **§ 35 Abs. 2 StGB** — Vermeidbarer entschuldigender Notstand: Milderung nach § 49 Abs. 1 StGB.

## Anwendungsfaelle § 49 Abs. 2 StGB (fakultativ)

- Selten als Verweis, haeufig in der Praxis bei Sondernormen, die "Strafmilderung nach § 49 Abs. 2 StGB" zulassen. Beispiele: § 13 Abs. 2 StGB (Unterlassen mit Garantenstellung).

## Berechnungsbeispiele

### Beispiel 1: Beihilfe zum Raub § 27 Abs. 2 i.V.m. § 49 Abs. 1 StGB

- Grundtatbestand § 249 Abs. 1 StGB: Freiheitsstrafe 1 Jahr bis 15 Jahre.
- Beihilfe-Milderung nach § 49 Abs. 1 StGB:
 - Hoechstmass: 3/4 von 15 Jahren = 11 Jahre 3 Monate.
 - Mindestmass: bei Mindeststrafe von 1 Jahr ermaessigt auf 3 Monate (Nr. 3).
- Konkreter Strafrahmen: 3 Monate bis 11 Jahre 3 Monate.

### Beispiel 2: Verminderte Schuldfaehigkeit § 21 StGB beim Totschlag § 212 StGB

- Grundtatbestand § 212 Abs. 1 StGB: 5 bis 15 Jahre.
- § 21 i.V.m. § 49 Abs. 1 StGB:
 - Hoechstmass: 3/4 von 15 Jahren = 11 Jahre 3 Monate.
 - Mindestmass: bei Mindeststrafe von 5 Jahren ermaessigt auf 2 Jahre (Nr. 3 erste Alt.).
- Konkreter Strafrahmen: 2 Jahre bis 11 Jahre 3 Monate.

### Beispiel 3: Mehrere Milderungsgruende — Beihilfe + § 21 StGB beim Totschlag

- Zwingende Milderung § 27 Abs. 2: 2 Jahre bis 11 Jahre 3 Monate (siehe Beispiel 2-Logik bei § 49 Abs. 1 StGB).
- Hinzu § 21 StGB: erneute Milderung nach § 49 Abs. 1 StGB:
 - Hoechstmass: 3/4 von 11 Jahren 3 Monaten = ca. 8 Jahre 5 Monate.
 - Mindestmass: bei Ausgangsmindeststrafe von 2 Jahren ermaessigt auf 6 Monate.
- Konkreter Strafrahmen nach Mehrfachmilderung: 6 Monate bis ca. 8 Jahre 5 Monate. **BGH-Aktenzeichen zur Berechnungstechnik der mehrfachen Milderung vor Zitat verifizieren in dejure.org/openjur.de.**

## Schritt-fuer-Schritt-Anleitung

1. Welche Strafmilderungsnorm liegt vor (§ 17, 21, 23 Abs. 2, 27 Abs. 2, 28 Abs. 1, 35 Abs. 2, 46a, 46b StGB)?
2. Verweist die Norm auf § 49 Abs. 1 oder Abs. 2 StGB?
3. Ist die Milderung **zwingend** oder **fakultativ** (kann/muss)?
4. Liegen **mehrere** Milderungsgruende vor? Reihenfolge der Anwendung?
5. Konkreten Strafrahmen ausrechnen.
6. In den so geschaffenen Strafrahmen die konkrete Strafe nach § 46 StGB einordnen.

## Typische Fehler

- **§ 49 Abs. 1 falsch berechnet**: Hoechstmass falsch (1/2 statt 3/4) oder Mindestmass nicht reduziert (Nr. 3-Tabelle nicht angewendet).
- **Milderung uebersehen**: Beihilfe nach § 27 Abs. 2 StGB ist **zwingend**.
- **Mehrere Milderungen** falsch verkettet: jede Milderung wird auf das Ergebnis der vorigen angewendet.
- **§ 49 Abs. 2 statt Abs. 1** verwendet, obwohl Norm Abs. 1 vorschreibt.
- **§ 46a StGB** ohne Pruefung, ob Strafrahmen "nicht ueber 1 Jahr" auch fuer den **konkret** drohenden Bereich gilt (siehe Fachmodul).

## Querverweise

- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen-Logik.
- `minder-schwerer-fall-und-besonders-schwerer-fall` — Strafrahmen-Modifikation neben § 49 StGB.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — § 46a Wechsel auf § 49 Abs. 1 StGB.
- `paragraph-46-stgb-grundsatz-strafzumessung` — Strafzumessung nach Strafrahmen-Bildung.

## Quellen und Stand 05/2026

- § 49 StGB in der geltenden Fassung.
- §§ 17, 21, 23 Abs. 2, 27 Abs. 2, 28, 35 Abs. 2, 46a, 46b StGB.
- BGH-Linie zur mehrfachen Milderung — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.

## 3. `strafrahmen-und-strafzumessungsstufen`

**Fokus:** Strafrahmen-Logik vor der konkreten Zumessung. Aufbau abstrakter Strafrahmen aus Grundtatbestand, Qualifikation, Privilegierung. Modifikationen durch Regelbeispiele und minder schweren Fall. Verschiebung durch §§ 49 Abs. 1 23 Abs. 2 28 Abs. 1 StGB. Aufbau konkreter Strafrahmen, Ableitung der konkreten Strafe nach § 46 StGB. Schnittstelle Strafmilderung und Strafzumessung.

# Strafrahmen und Strafzumessungsstufen

## Worum geht es?

Vor der konkreten Strafzumessung muss der **gesetzliche Strafrahmen** bestimmt werden. Erst danach wird innerhalb dieses Rahmens nach § 46 StGB die konkrete Strafe gebildet. Der Skill erlaeutert die Stufen: abstrakter Strafrahmen, Modifikationen, konkreter Strafrahmen, konkrete Strafe.

## Wann brauchen Sie diese Skill?

- Sie verteidigen oder klagen an und muessen bestimmen, welcher Strafrahmen anwendbar ist (Grundtatbestand, Qualifikation, minder schwerer Fall?).
- Sie pruefen, ob ein **besonders schwerer Fall** wegen eines Regelbeispiels anzunehmen ist.
- Sie sondieren in einer Verstaendigung, welcher Strafrahmen Verhandlungsgrundlage sein soll (§ 257c Abs. 3 StPO).

## Rechtliche Grundlagen

- **§ 38 StGB** — Freiheitsstrafe: 1 Monat bis 15 Jahre (zeitige); lebenslang.
- **§ 39 StGB** — Bemessung der Freiheitsstrafe (Monate; Jahre und Monate).
- **§ 40 StGB** — Geldstrafe in Tagessaetzen.
- **§ 49 StGB** — Besondere Milderungsgruende; Abs. 1 zwingend, Abs. 2 fakultativ; vgl. `strafmilderung-49-stgb-zwingend-fakultativ`.
- Spezialnormen mit Strafrahmen-Modifikation: §§ 243, 263 Abs. 3, 244, 250, 251, 211, 212, 213 StGB usw.

## Stufen der Strafrahmen-Bildung

### Stufe 1 — Abstrakter gesetzlicher Strafrahmen

Aus dem Grundtatbestand oder der Qualifikation. Beispiel:

- § 242 Abs. 1 StGB (Diebstahl): Freiheitsstrafe bis 5 Jahre oder Geldstrafe.
- § 243 Abs. 1 StGB (besonders schwerer Fall): Freiheitsstrafe 3 Monate bis 10 Jahre.
- § 244 Abs. 1 Nr. 1 StGB (Diebstahl mit Waffen, Bande, Wohnungseinbruch): Freiheitsstrafe 6 Monate bis 10 Jahre.
- § 244 Abs. 4 StGB (Wohnungseinbruchsdiebstahl in dauerhaft genutzte Privatwohnung): Freiheitsstrafe 1 bis 10 Jahre.

### Stufe 2 — Modifikationen

- **Minder schwerer Fall**: Senkung des Strafrahmens, z.B. § 213 StGB, § 249 Abs. 2 StGB. Vgl. `minder-schwerer-fall-und-besonders-schwerer-fall`.
- **Besonders schwerer Fall durch Regelbeispiel**: Anhebung; § 243 StGB (Diebstahl), § 263 Abs. 3 StGB (Betrug). Vgl. `regelbeispiele-rechtsprechung`.
- **Strafmilderung nach § 49 StGB**: zwingend (Abs. 1) oder fakultativ (Abs. 2); Verschiebung der Strafrahmen-Ober- und Untergrenze.
- **Versuch** (§ 23 Abs. 2 StGB): kann nach § 49 Abs. 1 StGB gemildert werden.
- **Beihilfe** (§ 27 Abs. 2 StGB): muss nach § 49 Abs. 1 StGB gemildert werden.
- **Persoenliche Merkmale** (§ 28 Abs. 1 StGB): Strafmilderung nach § 49 Abs. 1 StGB.
- **Verminderte Schuldfaehigkeit** (§ 21 StGB): kann nach § 49 Abs. 1 StGB gemildert werden.
- **Verbotsirrtum** vermeidbar (§ 17 Satz 2 StGB): kann gemildert werden.

### Stufe 3 — Konkreter Strafrahmen

Nach allen Modifikationen das Ergebnis. Beispiel:

- Grundtatbestand § 249 Abs. 1 StGB (Raub): Freiheitsstrafe 1 Jahr bis 15 Jahre.
- Minder schwerer Fall § 249 Abs. 2 StGB: 6 Monate bis 5 Jahre.
- Bei Beihilfe nach § 27 Abs. 2 i.V.m. § 49 Abs. 1 Nr. 2 StGB: Hoechstmass 3/4 von 5 Jahren = 3 Jahre 9 Monate.

### Stufe 4 — Konkrete Strafe

Innerhalb des konkreten Strafrahmens nach § 46 StGB. Hier kommen die Strafzumessungstatsachen ins Spiel; vgl. `strafzumessungs-tatsachen-46-ii-stgb`.

## Reihenfolge in der Pruefung (Standard)

1. Welche Tatbestaende sind verwirklicht?
2. Strafrahmen des einschlaegigen Tatbestands oder der Qualifikation.
3. Liegt minder schwerer Fall vor (Gesamtbetrachtung)?
4. Liegt Regelbeispiel oder unbenannter besonders schwerer Fall vor?
5. Liegen Milderungsgruende nach § 49 StGB vor? In welcher Reihenfolge greifen sie? (Mehrfache Milderung moeglich; jeweils auf das Ergebnis der vorigen Milderung anzuwenden.)
6. Konkreter Strafrahmen festhalten.
7. Konkrete Strafe nach § 46 StGB im Spielraum schuldangemessener Strafe.

## Sonderfall: Mehrfache Milderung

Wenn mehrere § 49 Abs. 1 StGB-Milderungen zusammentreffen (z.B. Beihilfe + verminderte Schuldfaehigkeit + Versuch), wird **kettenweise** gemildert: erst die eine Milderung anwenden, dann auf das Ergebnis die naechste. **Aktenzeichen der st. Rspr. vor Zitat verifizieren in dejure.org/openjur.de.**

## Typische Fehler

- **Regelbeispiel automatisch angenommen**: Auch wenn ein Regelbeispiel erfuellt ist, muss eine **Gesamtbetrachtung** ergeben, dass die "Indiz-Wirkung" nicht entkraeftet ist (BGH st. Rspr.; Az vor Zitat verifizieren).
- **§ 49 Abs. 1 StGB falsch berechnet**: Hoechstmass 3/4 (Freiheitsstrafe), Mindeststrafe entfaellt oder reduziert nach § 49 Abs. 1 Nr. 2 und 3 StGB. Bei lebenslang: 3 bis 15 Jahre (§ 49 Abs. 1 Nr. 1 StGB).
- **§ 28 StGB uebersehen** bei Beihilfe-/Anstifter-Pruefung: fehlende strafbegruendende persoenliche Merkmale fuehren zwingend zur Strafmilderung nach § 49 Abs. 1 StGB.
- **Doppelverwertung** zwischen Regelbeispiel und § 46 StGB: Umstaende, die das Regelbeispiel begruenden, duerfen nicht noch einmal als strafschaerfender Faktor angefuehrt werden.

## Querverweise

- `paragraph-46-stgb-grundsatz-strafzumessung` — Folge nach Strafrahmen-Bestimmung.
- `strafmilderung-49-stgb-zwingend-fakultativ` — Detail.
- `minder-schwerer-fall-und-besonders-schwerer-fall` — Detail.
- `regelbeispiele-rechtsprechung` — Detail.

## Quellen und Stand 05/2026

- §§ 38, 39, 49 StGB in der geltenden Fassung.
- Einschlaegige Spezialnormen je nach Tatbestand.
- BGH-Linie zu mehrfacher Milderung und Regelbeispielen — Aktenzeichen in dejure.org/openjur.de verifizieren.
- Quellenregel: vgl. `references/zitierweise.md`.
