---
name: eu-abgrenzung-einschlaegige-normen
description: "EU Abgrenzung Einschlaegige Normen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# EU Abgrenzung Einschlaegige Normen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **EU Abgrenzung Einschlaegige Normen** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `de-eu-recht-abgrenzung` | Klaert die Abgrenzung zwischen nationalem deutschen Recht und Unionsrecht: wann gilt AEUV/EUV/GRCh/Verordnung/Richtlinie unmittelbar, wann richtlinienkonforme Auslegung, wann Vorabentscheidungsersuchen Art. 267 AEUV und Anwendungsvorrang. |
| `einschlaegige-normen-vorschlagen-de` | Schlaegt anhand eines Lebenssachverhalts einschlaegige Normen des deutschen Rechts vor: BGB, HGB, StGB, StPO, ZPO, VwGO, GG, AO, SGB und Nebengesetze. Gibt Prüfungsreihenfolge und Hinweise auf Spezialitaet und konkurrierende Anspruchsgrundlagen. |
| `einschlaegige-normen-vorschlagen-eu` | Schlaegt einschlaegige Normen des Unionsrechts vor: AEUV, EUV, GRCh (Primaerrecht) sowie EU-Verordnungen und Richtlinien (Sekundaerrecht). Gibt Hinweise auf EuGH-Judikatur und Fundstellen bei curia.europa.eu. Klaert unmittelbare Wirkung und Anwendungsvorrang. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **EU Abgrenzung Einschlaegige Normen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `de-eu-recht-abgrenzung`

**Fokus:** Klaert die Abgrenzung zwischen nationalem deutschen Recht und Unionsrecht: wann gilt AEUV/EUV/GRCh/Verordnung/Richtlinie unmittelbar, wann richtlinienkonforme Auslegung, wann Vorabentscheidungsersuchen Art. 267 AEUV und Anwendungsvorrang.

# Deutsches Recht und Unionsrecht — Abgrenzung

## Zweck

Dieser Skill klärt, ob und in welchem Umfang Unionsrecht im konkreten Sachverhalt anzuwenden ist. Er unterscheidet Primärrecht (AEUV, EUV, GRCh), Sekundärrecht (Verordnungen, Richtlinien, Beschlüsse) und die Wechselwirkung mit nationalem Recht. Fehler bei dieser Abgrenzung führen regelmäßig zur Prüfung der falschen Norm.

## Triage zu Beginn

1. Liegt ein grenzüberschreitender oder EU-regulierter Sachverhalt vor?
2. Ist eine Behörde oder ein Mitgliedstaat beteiligt (Staatshaftung, Vertragsverletzung)?
3. Wird eine EU-Verordnung (unmittelbar anwendbar) oder eine Richtlinie (Umsetzungsakt?) berührt?
4. Könnte die GRCh greifen (Art. 51 Abs. 1: Durchführung von Unionsrecht)?
5. Besteht Kollision zwischen nationalem Recht und Unionsrecht?

## Prüfungsschritte

### Schritt 1 — Liegt ein unionsrechtlich geregelter Bereich vor?

Indizien für Unionsrechtsbezug:
- Grenzüberschreitender Sachverhalt (Personen, Waren, Dienstleistungen, Kapital)
- Erwähnung von DSGVO, Produkthaftungsrichtlinie, Verbraucherrechterichtlinie, KI-VO, Lieferkettensorgfaltspflichtengesetz mit EU-Bezug, Vergaberecht
- Tätigkeit einer EU-Institution oder Bezug auf EU-Fördermittel
- Diskriminierung aufgrund verbotener Merkmale (Art. 19 AEUV, Art. 21 GRCh)

### Schritt 2 — Welche Rechtsquelle gilt?

| Rechtsquelle | Geltung | Wirkung |
|-------------|---------|---------|
| AEUV / EUV (Primärrecht) | Unmittelbar, Vorrang | Höchstrangiges Unionsrecht; verdrängt nationales Recht |
| GRCh Art. 51 | Gilt bei Durchführung von Unionsrecht durch Mitgliedstaaten | Grundrechte der EU; Parallelprüfung zu GG |
| EU-Verordnung (Art. 288 Abs. 2 AEUV) | Unmittelbar und direkt anwendbar | Kein nationaler Umsetzungsakt erforderlich |
| EU-Richtlinie (Art. 288 Abs. 3 AEUV) | Nach Umsetzungsfrist; richtlinienkonforme Auslegung | Kein Horizontaleffekt zwischen Privaten (Grundsatz) |
| Beschlüsse | Nur für Adressaten verbindlich | Einzelfall |

### Schritt 3 — Anwendungsvorrang

Der Anwendungsvorrang des Unionsrechts bedeutet: Entgegenstehendes nationales Recht wird nicht nichtig, aber im Kollisionsfall unangewendet gelassen. Nationale Gerichte sind verpflichtet, nationales Recht unionsrechtskonform auszulegen und im Kollisionsfall Unionsrecht anzuwenden.

Leitentscheidungen: EuGH Rs. 6/64 (Costa/ENEL) und Rs. 106/77 (Simmenthal) — live zu prüfen unter curia.europa.eu.

**Grenze:** Der Anwendungsvorrang gilt nicht gegenüber dem GG-Kern (Ewigkeitsgarantie Art. 79 Abs. 3 GG) — BVerfG Solange II; Lissabon-Urteil (live zu prüfen unter bverfg.de).

### Schritt 4 — Richtlinienkonforme Auslegung

Bei Richtlinien, die noch umzusetzen sind oder deren Umsetzungsfrist abgelaufen ist:
- Nationales Recht ist richtlinienkonform auszulegen (EuGH, Rs. 14/83 — Von Colson; live zu prüfen)
- **Grenze:** Contra-legem-Auslegung ist unzulässig; das nationale Gericht kann nationale Normen nicht gegen ihren eindeutigen Wortlaut "umdeuten"

### Schritt 5 — Unmittelbare Wirkung von Richtlinien

Ausnahmsweise unmittelbare Wirkung einer nicht umgesetzten Richtlinie gegenüber dem Staat (vertikale Wirkung), wenn:
1. Umsetzungsfrist abgelaufen
2. Norm ist inhaltlich unbedingt und hinreichend bestimmt
3. Staat als Adressat (nicht Privatpersonen untereinander)

### Schritt 6 — Staatshaftung (Francovich)

Wenn keine unmittelbare Wirkung: Staatshaftungsanspruch möglich, wenn Mitgliedstaat eine Richtlinie nicht oder nicht richtig umsetzt und dem Einzelnen dadurch ein Schaden entsteht (EuGH Rs. C-6/90 und C-9/90 — Francovich; live zu prüfen unter curia.europa.eu).

## GRCh Art. 51 — Abgrenzung zum GG

Die Grundrechtecharta gilt nur, wenn Unionsrecht durchgeführt wird. Bei rein nationalem Sachverhalt bleibt das GG allein maßgeblich. Das System weist auf diese Abgrenzung hin und fragt nach dem Unionsbezug.

Parallelgrundrechte: Art. 7 GRCh / Art. 2 Abs. 1 GG (Privatleben); Art. 8 GRCh / Art. 2 Abs. 1 GG (Datenschutz); Art. 11 GRCh / Art. 5 GG (Meinungsfreiheit).

## Ausgabe

Entscheidungsbaum mit Schritt-für-Schritt-Prüfung: Liegt Unionsrechtsbezug vor? → Welche Rechtsquelle? → Anwendungsvorrang? → Richtlinienkonforme Auslegung nötig? → Vorabentscheidungsersuchen prüfen (→ Skill eu-vorabentscheidung-pruefen).

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern (curia.europa.eu, bverfg.de, dejure.org).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- EU-Normtext live prüfen: eur-lex.europa.eu (konsolidierte Fassungen), gesetze-im-internet.de (Umsetzungsgesetze).

## 2. `einschlaegige-normen-vorschlagen-de`

**Fokus:** Schlaegt anhand eines Lebenssachverhalts einschlaegige Normen des deutschen Rechts vor: BGB, HGB, StGB, StPO, ZPO, VwGO, GG, AO, SGB und Nebengesetze. Gibt Prüfungsreihenfolge und Hinweise auf Spezialitaet und konkurrierende Anspruchsgrundlagen.

# Einschlägige Normen vorschlagen — Deutsches Recht

## Triage zu Beginn — kläre vor der Normauswahl

1. Wer will was von wem woraus? (klassische Vier-Fragen-Methode)
2. Handelt es sich um einen privatrechtlichen, öffentlich-rechtlichen oder strafrechtlichen Sachverhalt?
3. Besteht eine vertragliche Beziehung zwischen den Beteiligten?
4. Hat der Sachverhalt einen grenzüberschreitenden Bezug? → IPR prüfen (Rom I/Rom II VO)
5. Sind schutzgesetzliche Spezialregelungen denkbar (ProdHG, StVG, HaftPflG, WpHG)?

## Zweck

Dieser Skill unterstützt den Nutzer bei der Identifikation einschlägiger Normen des deutschen Rechts anhand eines geschilderten Lebenssachverhalts. Das System macht Vorschläge auf der Grundlage des im Sachverhalt beschriebenen Rechtsgebiets und der typischen Anspruchsgrundlagen. Die endgültige Normwahl liegt beim Nutzer.

## Zentrale Paragrafenkette je Rechtsgebiet

- Vertragsrecht: §§ 433 ff., 535 ff., 611 ff., 631 ff. BGB — Spezialvorrang vor §§ 280 ff. BGB
- Delikt/Schadensersatz: § 823 Abs. 1 BGB (Verletzung absoluter Rechte), § 823 Abs. 2 i.V.m. Schutzgesetz, § 826 BGB, § 831 BGB
- Bereicherungsrecht: §§ 812 ff. BGB — subsidiär zu Vertrag
- Strafrecht: §§ 263, 266, 303, 223, 242, 249 StGB — Strafantrag bei Antragsdelikten (§ 77 StGB, 3 Monate)
- Verwaltungsrecht: § 35 VwVfG (VA-Definition), § 42 VwGO (Anfechtungs-/Verpflichtungsklage)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026: BGH VI ZR 188/17 geloescht – AZ existiert (19.01.2021, NJW 2021, 1818), betrifft aber Haftungsmassstab Sporttrainer (Tischtennis-Erste-Hilfe), nicht Einbeziehung AGB / Schutzgesetz § 823 Abs. 2 BGB (WRONG_TOPIC). BGH VI ZR 26/21 geloescht – AZ auf dejure.org nicht auffindbar (NOT_FOUND). -->

## Schritt-für-Schritt-Vorgehen

**Schritt 1 — Sachverhalts-Kategorisierung**

Das System kategorisiert den Sachverhalt nach Rechtsgebiet:

| Kategorie | Typische Normen |
|-----------|----------------|
| Vertragsrecht | §§ 433 ff. BGB (Kauf); §§ 611 ff. BGB (Dienst/Arbeitsvertrag); §§ 631 ff. BGB (Werkvertrag); §§ 535 ff. BGB (Miete) |
| Deliktsrecht | § 823 Abs. 1 BGB; § 823 Abs. 2 BGB i.V.m. Schutzgesetz; § 826 BGB; § 831 BGB |
| Bereicherungsrecht | §§ 812 ff. BGB — Leistungskondiktion, Nichtleistungskondiktion |
| Sachenrecht | Normtext, bereitgestellte Materialien, verifizierte Rechtsprechung |
| Strafrecht | § 263 StGB (Betrug); § 303 StGB (Sachbeschädigung); § 223 StGB (Körperverletzung); § 242 StGB (Diebstahl); § 266 StGB (Untreue) |
| Arbeitsrecht | KSchG; § 623 BGB (Schriftform Kündigung); ArbGG; MuSchG; AGG |
| Verwaltungsrecht | Normtext, amtliche Materialien, verifizierte Rechtsprechung |
| Sozialrecht | SGB I-XII; § 44 SGB X (Rücknahme); § 45 SGB X (Aufhebung) |
| Steuerrecht | § 38 AO (Entstehung der Steuerschuld); §§ 172 ff. AO (Bestandskraft) |
| Erbrecht | §§ 1922 ff. BGB; §§ 2303 ff. BGB (Pflichtteil) |
| Familienrecht | §§ 1353 ff. BGB; §§ 1601 ff. BGB (Unterhalt); §§ 1564 ff. BGB (Scheidung) |

**Schritt 2 — Normvorschlag mit Prüfungshinweis**

Das System nennt:
1. Primäre Anspruchsgrundlage (wahrscheinlichste Norm)
2. Konkurrierende Normen (Anspruchskonkurrenz oder -idealkonkurrenz)
3. Ausschlussnormen (Spezialität: z.B. Kaufgewährleistung § 437 BGB geht § 823 BGB vor, wenn nur Äquivalenzinteresse betroffen)
4. Vorfragen (z.B. Wirksamkeit des Vertrags, Geschäftsfähigkeit)

**Schritt 3 — Entscheidungsbaum Normwahl**

```
Besteht ein Vertrag?
├─ Ja → Vertragsrecht primär prüfen (§§ 280 ff. / spezifische Vertragstypen)
│ → Deliktshaftung parallel prüfen bei Rechtsgutsverletzung
└─ Nein → Delikt (§ 823 ff.) / Bereicherungsrecht (§ 812 ff.) / öffentl. Recht
 └─ Schutzgesetz i.S.d. § 823 Abs. 2 BGB? → Verletzter als Schutzzweck?
```

**Schritt 4 — Hinweis auf Rechtsprechung**

Das System weist darauf hin, dass für die Auslegung der vorgeschlagenen Normen aktuelle Rechtsprechung zu prüfen ist (BGH, BAG, BVerwG, BSG, BFH je nach Rechtsgebiet). Für aktuelle Entscheidungen: dejure.org, openjur.de, bundesgerichtshof.de, rechtsprechung-im-internet.de.

**Schritt 5 — Normwahl durch Nutzer bestätigen**

Das System listet Vorschläge auf und bittet den Nutzer, die zu prüfende Norm zu bestätigen oder eine andere Norm anzugeben. Erst nach Bestätigung wird die Norm in `norm-zerlegen-in-tatbestandsmerkmale` übergeben.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Grenzen

Das System weist ausdrücklich darauf hin, dass:
- Gesetzesänderungen nach dem Wissensstand nicht erfasst sind
- Landesrecht (z.B. Landesbauordnungen, kommunales Satzungsrecht) nur eingeschränkt vorgeschlagen werden kann
- Sondergesetze (z.B. EnWG, TKG, AMG, LFGB) nur grob kategorisiert werden

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

## 3. `einschlaegige-normen-vorschlagen-eu`

**Fokus:** Schlaegt einschlaegige Normen des Unionsrechts vor: AEUV, EUV, GRCh (Primaerrecht) sowie EU-Verordnungen und Richtlinien (Sekundaerrecht). Gibt Hinweise auf EuGH-Judikatur und Fundstellen bei curia.europa.eu. Klaert unmittelbare Wirkung und Anwendungsvorrang.

# Einschlägige Normen vorschlagen — Unionsrecht

## Zweck

Dieser Skill identifiziert einschlägige Normen des Unionsrechts anhand des geschilderten Sachverhalts. Er unterscheidet Primärrecht (AEUV, EUV, GRCh) und Sekundärrecht (Verordnungen, Richtlinien, Beschlüsse) und gibt Hinweise auf die einschlägige Rechtsprechung des EuGH und des EuG.

## Triage zu Beginn

1. Ist der Sachverhalt grenzüberschreitend oder EU-reguliert?
2. Handelt es sich um eine Beziehung Bürger–Staat (vertikale Konstellation) oder Bürger–Bürger (horizontal)?
3. Ist eine bestimmte Grundfreiheit oder ein Grundrecht der GRCh berührt?
4. Ist bereits ein nationales Umsetzungsgesetz einschlägig?
5. Liegt die fragliche Entscheidung nach dem Wissensstand des Systems? → Live-Check bei curia.europa.eu empfehlen

## Primärrecht — AEUV, EUV, GRCh

### Grundfreiheiten (AEUV)

| Grundfreiheit | Primärnormen | Typische Sachverhalte |
|--------------|-------------|----------------------|
| Warenverkehrsfreiheit | Art. 34–36 AEUV | Einfuhrverbote, technische Normen, Kennzeichnungspflichten |
| Arbeitnehmerfreizügigkeit | Art. 45–48 AEUV | Diskriminierung bei Einstellung/Lohn, Sozialleistungen |
| Niederlassungsfreiheit | Art. 49–55 AEUV | Zulassungsbeschränkungen für Berufe, Gesellschaftssitz |
| Dienstleistungsfreiheit | Art. 56–62 AEUV | Grenzüberschreitende Dienstleistungen, Entsendung |
| Kapital- und Zahlungsverkehrsfreiheit | Art. 63–66 AEUV | Kapitalverkehrskontrollen, Dividendenbesteuerung |

### Wettbewerbsrecht (AEUV)

| Bereich | Normen |
|---------|--------|
| Kartellverbot | Art. 101 AEUV |
| Marktmachtmissbrauch | Art. 102 AEUV |
| Beihilfenverbot | Art. 107–109 AEUV |

### Grundrechtecharta (GRCh)

Anwendbar bei Durchführung von Unionsrecht durch Mitgliedstaaten (Art. 51 Abs. 1 GRCh). Einschlägige Artikel: Art. 7 (Privatleben), Art. 8 (Datenschutz), Art. 11 (Meinungsfreiheit), Art. 15 (Berufsfreiheit), Art. 17 (Eigentum), Art. 21 (Gleichbehandlung), Art. 47 (effektiver Rechtsschutz), Art. 48 (Unschuldsvermutung).

## Sekundärrecht — Wichtige Verordnungen und Richtlinien

| Bereich | Rechtsakt | Fundstelle |
|---------|-----------|------------|
| Datenschutz | DSGVO (VO 2016/679) | eur-lex.europa.eu |
| Produkthaftung | RL 85/374/EWG; ab 2024: RL 2024/2853 | eur-lex.europa.eu |
| Verbraucherrecht | VRRL (RL 2011/83/EU); Klausel-RL (RL 93/13/EWG) | eur-lex.europa.eu |
| KI-Regulierung | KI-VO (VO 2024/1689) | eur-lex.europa.eu |
| Vergaberecht | RL 2014/24/EU; RL 2014/25/EU | eur-lex.europa.eu |
| Kartell | VO 1/2003; VO 330/2010 (Vertikal-GVO) | eur-lex.europa.eu |
| Finanzmarkt | MiFID II; CRR/CRD IV | eur-lex.europa.eu |

## EuGH-Judikatur — Fundstellen

Das System verweist auf Leitentscheidungen des EuGH, die für die vorgeschlagene Norm relevant sind:
- **curia.europa.eu** (amtliche Datenbank, Volltext, suchbar nach Rechtssache und Aktenzeichen)
- **eur-lex.europa.eu** (Rechtsakttexte, konsolidierte Fassungen)

**Wichtig:** Für aktuelle Entscheidungen ist eine manuelle Suche in curia.europa.eu erforderlich, da der Wissensstand des Systems ein festes Enddatum hat. Das System markiert Entscheidungen, die nach dem Wissensstand unsicher sind, als Prüfpunkte.

## Prüfung der unmittelbaren Wirkung

| Rechtssatz | Unmittelbare Wirkung? | Bedingungen |
|---|---|---|
| EU-Verordnung | Ja (Art. 288 Abs. 2 AEUV) | Kein Umsetzungsakt nötig |
| Richtlinie (Umsetzungsfrist abgelaufen) | Vertikal ja (Bürger gg. Staat) | Norm muss unbedingt und hinreichend bestimmt sein |
| Richtlinie (horizontal) | Nein (Grundsatz) | Nur richtlinienkonforme Auslegung; Ausnahme: Francovich-Haftung |
| Primärrecht (Grundfreiheiten) | Ja (vertikal und horizontal für Verbotsnormen) | EuGH ständige Rechtsprechung |

## Ausgabe

Das System nennt:
1. Einschlägige Primär- oder Sekundärrechtsnorm mit Artikelangabe
2. Unmittelbare Wirkung (Verordnung: ja; Richtlinie: nur bei staatlichem Handeln nach Ablauf der Umsetzungsfrist)
3. Anwendungsvorrang gegenüber nationalem Recht
4. Leitentscheidung des EuGH (als Prüfpunkt markiert; live zu prüfen unter curia.europa.eu)
5. Empfehlung zur Rechtsprechungsrecherche

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern (curia.europa.eu, eur-lex.europa.eu).
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: eur-lex.europa.eu (EU-Recht), gesetze-im-internet.de (Umsetzungsgesetze).
