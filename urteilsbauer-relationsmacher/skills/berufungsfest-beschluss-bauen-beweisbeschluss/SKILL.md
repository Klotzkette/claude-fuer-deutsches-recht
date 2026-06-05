---
name: berufungsfest-beschluss-bauen-beweisbeschluss
description: "Berufungsfest Beschluss Bauen Beweisbeschluss: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Berufungsfest Beschluss Bauen Beweisbeschluss

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Berufungsfest Beschluss Bauen Beweisbeschluss** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `berufungsfest-pruefen` | Fertiges Urteil gegen häufigste Aufhebungsgründe selbst prüfen: Richter will vor Urteilsversand Aufhebungsrisiken minimieren. Normen: § 529 ZPO (Tatsachenfeststellung Berufung), § 546 ZPO (Rechtsverletzung), § 547 Nr. 6 ZPO (Begründungsmangel). Prüfraster: Tatsachenfeststellung vollständig, kein Verfahrensmangel, keine uebergangenen Angriffs-/Verteidigungsmittel, Begründungstiefe ausreichend. Output Berufungsfest-Checkliste mit Ampelstatus. Abgrenzung: Revisionsfestigkeitsprüfung siehe revisionsfest-prüfen; Tenorierung siehe tenor-bauen-zivil. |
| `beschluss-bauen-zpo` | Zivilrechtliche Beschluesse erstellen: PKH, Streitwert, Beweis, Hinweis nach § 139 ZPO, Kostenfestsetzung, Versaeumnis, Erledigung. Normen: §§ 127 und 329 und 358 ff. sowie 139 und 103 ff. ZPO. Prüfraster: Unterschied Beschluss/Urteil (Begründungstiefe, Rechtsmittel), Tenor-Klarheit, Rechtsmittelbelehrung, Zustellung. Output Beschluss-Entwurf mit Tenor, Begründung, Rechtsmittelbelehrung. Abgrenzung: Urteil siehe entscheidungsgründe-zivil-schreiben; Vollstreckbarkeit siehe vorlaeufige-vollstreckbarkeit. |
| `beweisbeschluss-vorbereiten` | Beweisbeschluss nach § 359 ZPO vorbereiten: Richter bestimmt Beweisaufnahme nach muendlicher Verhandlung. Normen: § 359 ZPO (Inhalt Beweisbeschluss), § 286 ZPO (Beweislast), §§ 373 ff. ZPO (Zeugen), §§ 402 ff. ZPO (Sachverständige). Prüfraster: streitige Beweistatsachen, Beweisthema, Beweismittel, Beweislast, Reihenfolge Beweisaufnahme. Output Beweisbeschluss-Entwurf mit Beweisthemen-Tabelle. Abgrenzung: Beweiswürdigung danach siehe beweiswürdigung-mit-richter-input; Beschluss-Bau allgemein siehe beschluss-bauen-zpo. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Berufungsfest Beschluss Bauen Beweisbeschluss**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `berufungsfest-pruefen`

**Fokus:** Fertiges Urteil gegen häufigste Aufhebungsgründe selbst prüfen: Richter will vor Urteilsversand Aufhebungsrisiken minimieren. Normen: § 529 ZPO (Tatsachenfeststellung Berufung), § 546 ZPO (Rechtsverletzung), § 547 Nr. 6 ZPO (Begründungsmangel). Prüfraster: Tatsachenfeststellung vollständig, kein Verfahrensmangel, keine uebergangenen Angriffs-/Verteidigungsmittel, Begründungstiefe ausreichend. Output Berufungsfest-Checkliste mit Ampelstatus. Abgrenzung: Revisionsfestigkeitsprüfung siehe revisionsfest-prüfen; Tenorierung siehe tenor-bauen-zivil.

# Berufungsfestigkeit prüfen

## Triage zu Beginn — kläre vor dem Selbstcheck

1. Ist das Urteil bereits vollständig ausformuliert und unterzeichnet?
2. Wurde die Hinweispflicht (§ 139 ZPO) im gesamten Verfahren beachtet?
3. Sind alle Anträge beschieden (§ 308 ZPO — ne ultra petita)?
4. Ist der Tenor vollstreckungsfähig und bestimmt genug?
5. Besteht eine Berufungszulassungsfrage (§ 511 Abs. 4 ZPO — Streitwert unter 600 EUR)?

## Aktuelle Rechtsprechung zu Berufungsgründen

## Zentrale Normen

- § 529 ZPO — Tatsachenfeststellung als Grundlage des Berufungsgerichts
- § 546 ZPO — Revisionsgrund: fehlerhafte Rechtsanwendung
- § 547 ZPO — Absolute Revisionsgründe (Nr. 6: fehlende Begründung)
- § 139 ZPO — Hinweispflicht des Gerichts
- § 511 ZPO — Statthaftigkeit der Berufung; Beschwer 600 EUR
- § 538 Abs. 2 ZPO — Zurückverweisung durch Berufungsgericht bei Verfahrensmangel

## Haeufige Aufhebungsgründe

1. **Fehlerhafte Tatsachenfeststellung** (§ 529 ZPO) — konkrete Anhaltspunkte für Unrichtigkeit
2. **Verfahrensmangel** — Verstoß gegen rechtliches Gehör (Art. 103 Abs. 1 GG), falsche Beweisaufnahme, falsche Zuständigkeit
3. **Falsche Rechtsanwendung** (§ 546 ZPO)
4. **Begründungsmangel** — § 547 Nr. 6 ZPO absoluter Revisionsgrund
5. **Verletzung der Hinweispflicht** § 139 ZPO
6. **Nichtberücksichtigung erheblichen Vorbringens** — § 286 ZPO Verletzung freier Beweiswürdigung

## Checkliste vor Verkündung

- [ ] Sind alle Anträge beschieden?
- [ ] Sind alle erheblichen Tatsachen festgestellt?
- [ ] Beweisaufnahme im Tatbestand erwähnt?
- [ ] Beweiswürdigung in den Entscheidungsgründen mit konkreter Würdigung?
- [ ] Konkrete Bezugnahmen statt pauschaler Verweise (§ 313 Abs. 2 S. 2 ZPO)?
- [ ] Tenor vollstreckbar und bestimmt?
- [ ] Kostenentscheidung rechnerisch richtig?
- [ ] Vorläufige Vollstreckbarkeit angeordnet?
- [ ] Streitwert festgesetzt (§ 63 GKG)?
- [ ] Berufungszulassung erforderlich (§ 511 Abs. 4 ZPO)?
- [ ] Rechtsmittelbelehrung beigefügt (§ 232 ZPO)?
- [ ] Unterschrift der erkennenden Richter (§ 315 Abs. 1 ZPO)?
- [ ] Hinweispflicht § 139 ZPO dokumentiert?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `beschluss-bauen-zpo`

**Fokus:** Zivilrechtliche Beschluesse erstellen: PKH, Streitwert, Beweis, Hinweis nach § 139 ZPO, Kostenfestsetzung, Versaeumnis, Erledigung. Normen: §§ 127 und 329 und 358 ff. sowie 139 und 103 ff. ZPO. Prüfraster: Unterschied Beschluss/Urteil (Begründungstiefe, Rechtsmittel), Tenor-Klarheit, Rechtsmittelbelehrung, Zustellung. Output Beschluss-Entwurf mit Tenor, Begründung, Rechtsmittelbelehrung. Abgrenzung: Urteil siehe entscheidungsgründe-zivil-schreiben; Vollstreckbarkeit siehe vorlaeufige-vollstreckbarkeit.

# Beschluss bauen — Zivilprozess

## Zweck

Beschlüsse sind selbstständige Entscheidungen, die nicht auf muendliche Verhandlung ergehen müssen (Paragraf 128 IV ZPO). Sie sind das tägliche Werkzeug des Zivilrichters — von der prozessleitenden Maßnahme bis zur Endentscheidung im Beschlussverfahren (z.B. Familiensachen FamFG). Dieser Skill liefert die Form, die typischen Tenoere, die wichtigsten Begründungsmuster und die wiederkehrenden Fallstricke.

## 1) Beschluss-Typen im Überblick

| Typ | Norm | Anlass | Rechtsmittel |
|---|---|---|---|
| PKH-Beschluss | Paragraf 114 ff. ZPO | Antrag auf Prozesskostenhilfe | sofortige Beschwerde Paragraf 127 II ZPO |
| Verfahrenskostenhilfe Familiensachen | Paragraf 76 FamFG | VKH in FamFG-Sachen | sofortige Beschwerde Paragraf 76 II FamFG |
| Streitwertbeschluss | Paragraf 63 GKG | Festsetzung gegen Streitwertfestsetzung | Beschwerde Paragraf 68 GKG |
| Beweisbeschluss | Paragraf 358 ZPO | Anordnung einer Beweisaufnahme | unanfechtbar |
| Hinweisbeschluss | Paragraf 139 ZPO | rechtliche/tatsächliche Hinweise | unanfechtbar (aber gehörtspflicht-relevant) |
| Kostenfestsetzungsbeschluss | Paragraf 104 ZPO | Höhe der zu erstattenden Kosten | sofortige Beschwerde Paragraf 11 RPflG |
| Saeumnisbeschluss/Versäumnisurteil ohne Verhandlung | Paragraf 331 III ZPO | schriftliches Vorverfahren | Einspruch Paragraf 338 ZPO |
| Erledigungsbeschluss | Paragraf 91a ZPO | übereinstimmende Erledigungserklärung | sofortige Beschwerde Paragraf 91a II ZPO |
| Anerkenntnisbeschluss bei Mahnverfahren | Paragraf 700 ZPO | Anerkenntnis nach Widerspruch | wie Urteil |
| Vergleichsfeststellung | Paragraf 278 VI ZPO | gerichtlicher Vergleich auf Vorschlag | keiner |
| Zurueckweisungsbeschluss Berufung | Paragraf 522 II ZPO | offensichtlich unbegründet | keiner |
| Hinweis- und Aufklärungsbeschluss BGH | Paragraf 552a ZPO | Revision offensichtlich unbegründet | keiner |

## 2) Form

### Rubrum

Wie beim Urteil:
- **Aktenzeichen** in der oberen Zeile
- **Gericht** (Amtsgericht ..., Zivilkammer ..., Landgericht ...)
- **Parteien** mit Bezeichnung, Anschrift, Prozessbevollmaechtigte
- Bei Mehrparteien-Beschluss alle Beteiligten

### Überschrift

`**Beschluss**` (zentriert), nicht "Urteil", nicht "Verfügung"

### Tenor

Klar, knapp, vollstreckbar. **Imperative Form**, keine Konditionalsätze.

### Gründe

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Rechtsmittelbelehrung

Soweit Rechtsmittel statthaft ist (Paragraf 232 ZPO Pflicht). Bei unanfechtbaren Beschlüssen optional, aber nicht schaedlich.

### Unterschrift

Bei Einzelrichter eine Unterschrift, bei Kammer drei. Bei Beschluss nach Paragraf 522 II ZPO drei Unterschriften der Berufungssenats-Mitglieder.

## 3) Tenor-Bausteine

### PKH-Beschluss

```
Dem Klaeger wird fuer den ersten Rechtszug Prozesskostenhilfe ohne
Ratenzahlung bewilligt. Rechtsanwalt [Name] wird beigeordnet.
```

oder bei Teilbewilligung:

```
Dem Klaeger wird fuer den ersten Rechtszug Prozesskostenhilfe insoweit
bewilligt, als er Anspruch auf Zahlung von 5.000,- EUR nebst Zinsen
geltend macht. Im uebrigen wird der Antrag zurueckgewiesen, da
hinreichende Erfolgsaussicht (Paragraf 114 ZPO) fehlt.
```

### Streitwertbeschluss

```
Der Streitwert wird auf 12.500,- EUR festgesetzt.
```

Bei mehreren Streitgegenständen:

```
Der Streitwert wird festgesetzt
- fuer den Hauptantrag (Zahlung) auf 10.000,- EUR,
- fuer den Hilfsantrag (Feststellung) auf 2.500,- EUR.
```

### Beweisbeschluss

```
Es soll Beweis erhoben werden ueber die streitige Frage,
ob der Beklagte am 12. Juli 2024 in der Strasse [...] das vom
Klaeger gefuehrte Fahrzeug beschaedigt hat, durch
Vernehmung der Zeugen
1. ... (Anschrift: ...)
2. ... (Anschrift: ...)
und durch Einholung eines Sachverstaendigengutachtens zur
Hoehe des am Fahrzeug entstandenen Schadens.
```

### Hinweisbeschluss Paragraf 139 ZPO

```
Die Parteien werden auf folgende rechtliche Gesichtspunkte hingewiesen
(Paragraf 139 II ZPO):
1. Es bestehen Bedenken gegen die Schluessigkeit der Klage hinsichtlich
 des Vortrags zur Hoehe des Schmerzensgeldes. Der Klaeger wird
 gebeten, [...] naeher darzulegen.
2. [...]
Den Parteien wird Gelegenheit gegeben, hierzu binnen drei Wochen
schriftsaetzlich Stellung zu nehmen.
```

### Kostenfestsetzungsbeschluss

```
Die vom Beklagten an den Klaeger zu erstattenden Kosten werden auf
2.347,86 EUR festgesetzt. Hieraus sind 5 Prozentpunkte ueber dem
Basiszinssatz seit Rechtshaengigkeit (Paragraf 104 I 2 ZPO) zu zahlen.
```

### Erledigungsbeschluss Paragraf 91a ZPO — **nur bei übereinstimmender Erledigungserklärung**

Der Erledigungsbeschluss nach Paragraf 91a ZPO ergeht **nur**, wenn **beide Parteien** den Rechtsstreit übereinstimmend für erledigt erklärt haben. Er enthält **nur die Kostenentscheidung**.

```
Die Kosten des Rechtsstreits werden gegeneinander aufgehoben
(Paragraf 91a I 1 ZPO).
```

oder z.B.

```
Die Kosten des Rechtsstreits traegt der Beklagte (Paragraf 91a I 1 ZPO).
```

> **Achtung — abgrenzende Konstellation**: Bei **einseitiger** Erledigungserklärung, der die Gegenseite **widerspricht**, ist der Streitgegenstand gewandelt zur Feststellung der Erledigung. Darüber wird **durch Urteil** entschieden (nicht durch Beschluss nach Paragraf 91a ZPO), mit Tenor "Es wird festgestellt, dass die Hauptsache erledigt ist" und voller Kostenentscheidung nach Paragraf 91 ZPO. Tenor und Urteilsbegründung gehören dann nicht in diesen Beschluss-Skill, sondern in `tenor-bauen-zivil` und `entscheidungsgruende-zivil-schreiben`.

## 4) Begründungsmuster

### PKH — Erfolgsaussicht und Bedürftigkeit

```
Der Antrag hat Erfolg. Die Klage hat hinreichende Erfolgsaussicht
(Paragraf 114 ZPO), da der Klaeger fuer den von ihm geltend gemachten
Anspruch aus Paragraf 280 I, III, 281 BGB schluessig dargelegt
hat, dass [...]. Der Klaeger ist beduerftig im Sinne des Paragraf 115 ZPO;
seine Einkommensverhaeltnisse sind durch die eingereichte
Erklaerung gemaess Paragraf 117 ZPO belegt. Mutwilligkeit liegt nicht vor.
```

### Streitwertbeschluss — Bewertung

```
Der Streitwert ergibt sich aus dem Wert des Hauptantrags
(Paragraf 39 GKG). Die geltend gemachte Zahlung von 12.500,- EUR
bildet den Streitgegenstand, da Zinsen und Nebenforderungen
unberuecksichtigt bleiben (Paragraf 4 ZPO).
```

### Hinweis nach Paragraf 522 II ZPO

```
Der Senat beabsichtigt, die Berufung gemaess Paragraf 522 II 1 ZPO
durch Beschluss zurueckzuweisen, da
1. die Berufung keine Aussicht auf Erfolg hat (Paragraf 522 II 1 Nr. 1 ZPO),
2. die Rechtssache keine grundsaetzliche Bedeutung hat (Nr. 2),
3. die Fortbildung des Rechts oder die Sicherung einer einheitlichen
 Rechtsprechung eine Entscheidung des Berufungsgerichts nicht erfordert
 (Nr. 3) und
4. eine muendliche Verhandlung nicht geboten ist (Nr. 4).

Im einzelnen: [...]

Den Parteien wird Gelegenheit zur Stellungnahme bis [Datum]
gegeben.
```

## 5) Unterschied zum Urteil

- Beschluss ergeht **ohne** muendliche Verhandlung (Paragraf 128 IV ZPO), Urteil grundsaetzlich **mit** (Paragraf 128 I ZPO).
- Begründung beim Beschluss kuerzer — aber nicht unkenntlich.
- Rechtsmittel beim Beschluss ist meist die **sofortige Beschwerde** (Paragraf 567 ZPO, 2-Wochen-Frist), nicht die Berufung.
- **Tatbestand entfaellt** beim Beschluss in der Regel; bei Endentscheidungen (z.B. Versäumnisbeschluss Paragraf 331 III ZPO) ist eine knappe Sachverhaltsdarstellung sinnvoll.
- Beschlüsse koennen vom **Vorsitzenden allein** ergehen, soweit nicht Kammerentscheidung vorgeschrieben (Paragraf 348 ZPO Einzelrichter).

## 6) Typische Fehler

1. **Tenor unvollstreckbar.** Tenor muss aus sich heraus vollstreckbar sein. "Der Antrag wird teilweise zurueckgewiesen" reicht nicht — der zugesprochene Teil ist zu bezeichnen.
2. **PKH-Beschluss ohne Beiordnung.** Bei Anwaltszwang (LG, OLG, FamG mit Anwaltszwang) muss die Beiordnung mit ausgesprochen werden (Paragraf 121 ZPO).
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Streitwertbeschluss zu spaet.** Festsetzung bis zur nächsten Instanz möglich, aber meist mit Urteil/Endbeschluss (Paragraf 63 II GKG).
5. **Erledigungsbeschluss ohne Begründung der Kostenentscheidung.** Paragraf 91a ZPO verlangt billiges Ermessen; mindestens kurze Begründung der Kostenquote.
6. **Rechtsmittelbelehrung falsch.** Bei sofortiger Beschwerde 2 Wochen ab Zustellung; bei Einspruch gegen Versäumnisbeschluss 2 Wochen ab Zustellung; bei Beschwerde gegen Streitwertfestsetzung 6 Monate ab Festsetzung (Paragraf 68 GKG).
7. **Unterschriften fehlen.** Bei Kammer-Beschluss alle drei Richter. Bei Verhinderung Vermerk "für den an der Unterschrift verhinderten Richter [Name] gemäß Paragraf 315 ZPO".

## 7) Schnellprüfung vor Versand

- [ ] Aktenzeichen korrekt?
- [ ] Parteien vollständig bezeichnet?
- [ ] Tenor aus sich heraus vollstreckbar?
- [ ] Norm-Stütze für den Tenor (z.B. "Paragraf 91a I ZPO")?
- [ ] Begründung ausreichend für das Beschwerdegericht?
- [ ] Rechtsmittelbelehrung mit Frist und Form?
- [ ] Unterschrift(en) vollständig?

## Anschluss

- `relation-zivil` — bei nachfolgender Hauptsachenentscheidung
- `tenor-bauen-zivil` — Tenor-Werkstatt
- `vorlaeufige-vollstreckbarkeit` — bei verbundenem Urteil

## 3. `beweisbeschluss-vorbereiten`

**Fokus:** Beweisbeschluss nach § 359 ZPO vorbereiten: Richter bestimmt Beweisaufnahme nach muendlicher Verhandlung. Normen: § 359 ZPO (Inhalt Beweisbeschluss), § 286 ZPO (Beweislast), §§ 373 ff. ZPO (Zeugen), §§ 402 ff. ZPO (Sachverständige). Prüfraster: streitige Beweistatsachen, Beweisthema, Beweismittel, Beweislast, Reihenfolge Beweisaufnahme. Output Beweisbeschluss-Entwurf mit Beweisthemen-Tabelle. Abgrenzung: Beweiswürdigung danach siehe beweiswürdigung-mit-richter-input; Beschluss-Bau allgemein siehe beschluss-bauen-zpo.

# Beweisbeschluss vorbereiten

Vor der Beweisaufnahme das, was streitig und beweisbedürftig ist, förmlich festhalten.


## Triage zu Beginn

1. Welche Tatsachen sind zwischen den Parteien streitig und entscheidungserheblich?
2. Welche Beweismittel sind angeboten (Zeuge, Sachverständiger, Urkunde, Augenschein, Parteivernehmung)?
3. Wer trägt die Beweislast für welche Tatsache?
4. Ist Beweis bereits ganz oder teilweise erhoben — was steht noch aus?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 286 ZPO — freie richterliche Beweiswürdigung, Vollüberzeugung
- § 358, 359 ZPO — Beweisbeschluss (Inhalt: Beweisthema, Beweismittel, Beweisführer)
- § 373 ff. ZPO — Zeugenbeweis
- § 402 ff. ZPO — Sachverständigenbeweis
- § 291 ZPO — offenkundige Tatsachen (kein Beweis nötig)
- § 280 Abs. 1 S. 2 BGB — Beweislastumkehr bei Pflichtverletzung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Streitige Tatsachen identifizieren:** aus der Relation oder Aktenübersicht die entscheidungserheblichen, streitigen Tatsachen auflisten.
2. **Beweislast klären:** Grundsatz — Kläger für anspruchsbegründende, Beklagter für anspruchsvernichtende Tatsachen.
3. **Beweismittel zuordnen:** für jede streitige Tatsache: welches Beweismittel, von wem angeboten?
4. **Beweisbeschluss formulieren:** Beweisthema in einem Satz, Beweismittel, Beweisführer, Terminierung.
5. **Reihenfolge festlegen:** logische Reihenfolge (z.B. erst Grundtatbestand, dann Schaden).

## Output-Template

**Adressat:** Gerichtsinterne Notiz / Beweisbeschluss nach § 359 ZPO — Tonfall: sachlich-juristisch

```
BEWEISBESCHLUSS

In Sachen [KLÄGER] ./. [BEKLAGTER] — AZ: [AKTENZEICHEN]

wird Beweis erhoben über die Behauptung der [PARTEI],
[BEWEISTHEMA IN EINEM SATZ],
durch Vernehmung des Zeugen [NAME, ANSCHRIFT] / Einholung eines Sachverständigengutachtens
über das Thema: [GUTACHTENTHEMA].

Beweisführer: [PARTEI].
Termin: [DATUM].
```

## Voraussetzungen

1. **Streitige Tatsache** - nicht aus eigener Kenntnis des Gerichts und nicht unstreitig.
2. **Erheblich** - kommt es auf die Tatsache für den Anspruch an?
3. **Beweisbedürftig** - keine offenkundige Tatsache (Paragraf 291 ZPO), keine Beweislastumkehr greift.

## Inhalt nach Paragraf 359 ZPO

1. Streitige Tatsache(n) - Beweisthema
2. Beweismittel (Zeuge mit Name und Adresse / Sachverständiger / Augenschein / Urkunde / Parteivernehmung)
3. Beweisführer (welche Partei)
4. Reihenfolge

## Beweislast

- Kläger trifft Beweislast für anspruchsbegründende Tatsachen.
- Beklagter für anspruchshindernde / -vernichtende Tatsachen und für Einreden.
- Beweislastumkehr in Spezialgesetzen (Paragraf 280 I 2 BGB, ProdHG, Paragraf 7 StVG bei Halterhaftung).

## Beweismass

Paragraf 286 ZPO - volle Überzeugung des Gerichts. Wahrscheinlichkeit alleine reicht nicht.

---

<!-- AUDIT 27.05.2026 -->
> **Audit-Hinweis (27.05.2026):** BGH VI ZR 255/03, NJW 2005, 354 entfernt. Tatsaechliche Fundstelle NJW 2005, 354 gehoert zu BGH VI ZR 335/03 (Urt. v. 30.11.2004) — Thema: Haftungsprivileg § 828 Abs. 2 BGB bei Kind mit Kickboard gegen parkendes Fahrzeug; kein Bezug zu Anscheinsbeweis im Haftpflichtrecht. Aktenzeichen VI ZR 255/03 existiert unter dejure.org/2004,220 und betrifft Schmerzensgeld bei Persoenlichkeitsrechtsverletzung (Caroline-Tochter). Quelle: dejure.org/2004,220, dejure.org/?Text=NJW+2005,354.
