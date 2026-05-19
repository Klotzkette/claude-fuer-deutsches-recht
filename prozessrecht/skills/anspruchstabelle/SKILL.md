---
name: anspruchstabelle
description: Aufbau oder Überprüfung einer Anspruchstabelle – zivilrechtliche Element-für-Element-Analyse eines Anspruchs oder einer Einrede, oder patentrechtliche Verletzungs-/Nichtigkeitstabelle – mit Quellenbelegen für jedes Element und Lückenerkennung als Prioritätsausgabe. Verwenden, wenn der Nutzer eine Anspruchstabelle, Elementtabelle, Beweistabelle, patenrechtliche Verletzungsanalyse oder fragt „Was fehlt uns noch, um [Anspruch] zu beweisen?".
language: de
triggers:
  - "anspruchstabelle"
  - "elementtabelle"
  - "anspruchsprüfung"
  - "was fehlt zum beweis"
  - "patentverletzung chart"
  - "tatbestandsmerkmale"
---

# Anspruchstabelle

## Zweck

Systematische Prüfung und Visualisierung aller Tatbestandsmerkmale eines zivilrechtlichen Anspruchs oder einer Einrede (z. B. § 280 Abs. 1, 3, § 281 BGB; § 823 Abs. 1 BGB; § 1 UWG) oder einer patentrechtlichen Verletzungsanalyse (Anspruchsmerkmal für Anspruchsmerkmal). Das Plugin erstellt eine Tabelle mit dem aktuellen Beweisstand, markiert Lücken und gibt Handlungsempfehlungen zur Schließung offener Punkte.

Zwei Modi:
- `--zivil`: Zivilrechtliche Ansprüche und Einreden (BGB, HGB, UWG, MarkenG etc.)
- `--patent`: Patentrechtliche Verletzungs- (§§ 9 ff. PatG) oder Nichtigkeitsanalyse (§ 22 PatG i. V. m. §§ 1–5 PatG)

## Eingaben

- Aktives Mandat (Slug)
- Modus: `--zivil [Anspruchsnorm]` oder `--patent [--verletzung | --nichtigkeit] [Patentanspruch-Nr.]`
- Relevante Dokumente (Vertrag, Korrespondenz, Zeugenliste, Sachverständigengutachten, Patentschrift, angegriffene Ausführungsform)
- Aktueller Beweisstand (was liegt vor, was ist streitig)

## Ablauf

### Modus Zivilrecht (`--zivil`)

1. **Norm zerlegen:** Tatbestandsmerkmale des Anspruchs vollständig aufführen (z. B. § 280 Abs. 1 BGB: Schuldverhältnis, Pflichtverletzung, Vertretenmüssen, Schaden, Kausalität). Einreden und Einwendungen des Gegners separat tabellarisieren.

2. **Beweisstand erfassen:** Für jedes Element: belegt/unbelegt/streitig; vorhandene Beweismittel (Urkunde, Zeugenaussage, Sachverständigengutachten, Geständnisfiktion § 138 Abs. 3 ZPO, Augenschein § 371 ZPO) eintragen.

3. **Beweislast prüfen:** Wer trägt für welches Element die Darlegungs- und Beweislast? (Grundsatz: Anspruchsteller trägt für anspruchsbegründende Merkmale, § 363 BGB; Anspruchsgegner für rechtshindernde/rechtsvernichtende Merkmale – BGH, Urt. v. 05.10.2022 – VIII ZR 307/20, NJW 2023, 142 Rn. 31.)

4. **Lücken markieren:** Fehlende Belege und Beweismittel als **[LÜCKE]** mit Handlungsempfehlung (z. B. „Beauftragung Sachverständiger", „Auskunftsklage § 242 BGB / § 254 ZPO", „§ 142 ZPO Antrag auf Urkundenvorlage").

5. **Gegenargumente eintragen:** Bekannte oder antizipatierte Gegenargumente in Gegenargument-Spalte.

6. **Zusammenfassung:** Gesamtbewertung des Beweisrisikos (stark / mittel / schwach) mit Begründung.

### Modus Patent (`--patent`)

1. **Anspruch merkmalsweise aufgliedern** (Feature-by-Feature gemäß EPA-Praxis / BGH „Schneidmesser"-Methode: BGH, Urt. v. 06.05.2009 – Xa ZR 103/08, GRUR 2009, 837 – „Aufweichwanne").
2. **Angegriffene Ausführungsform** jedem Merkmal gegenüberstellen (wortsinngemäße oder äquivalente Verwirklichung, BGH, Urt. v. 12.03.2002 – X ZR 168/00, BGHZ 150, 149 Rn. 30 ff. – „Schneidmesser II").
3. **Nichtigkeitsangriff** (wenn `--nichtigkeit`): Neuheitsschädlicher Stand der Technik pro Merkmal (§ 3 PatG), erfinderische Tätigkeit (§ 4 PatG) – Aufgabe-Lösungs-Ansatz (BGH, Urt. v. 20.12.2011 – X ZR 53/08, GRUR 2012, 378 – „Installiereinrichtung II").
4. **Lücken und Risiken:** Unklare Merkmale, fehlende Dokumente zur angegriffenen Ausführungsform.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

Zivilrecht:
- BGH, Urt. v. 05.10.2022 – VIII ZR 307/20, NJW 2023, 142 Rn. 31 (Beweislastverteilung § 280 BGB).
- BGH, Urt. v. 23.09.2020 – XII ZR 86/18, NJW 2021, 228 Rn. 18 (Darlegungs- und Beweislast bei Pflichtverletzung).
- Ernst, in: MüKoBGB, 9. Aufl. 2022, § 280 Rn. 154 ff. (Anspruchsvoraussetzungen und Beweislast).
- Grüneberg, in: Grüneberg, BGB, 84. Aufl. 2025, § 280 Rn. 34 ff.

Patent:
- BGH, Urt. v. 06.05.2009 – Xa ZR 103/08, GRUR 2009, 837 – „Aufweichwanne" (merkmalsweise Auslegung des Patentanspruchs).
- BGH, Urt. v. 12.03.2002 – X ZR 168/00, BGHZ 150, 149 – „Schneidmesser II" (äquivalente Verletzung).
- BGH, Urt. v. 20.12.2011 – X ZR 53/08, GRUR 2012, 378 – „Installiereinrichtung II" (Aufgabe-Lösungs-Ansatz).
- Mes, PatG, 5. Aufl. 2020, § 9 Rn. 22 ff.
- Schulte/Voß, PatG, 10. Aufl. 2017, § 9 Rn. 48 ff.

## Ausgabeformat

### Zivilrechtliche Anspruchstabelle

**Anspruch:** Schadensersatz wegen Pflichtverletzung (§§ 280 Abs. 1, 3, 281 Abs. 1 BGB)

| Nr. | Tatbestandsmerkmal | Beweislast | Beweismittel (vorhanden) | Status | Lücke / Maßnahme |
|---|---|---|---|---|---|
| 1 | Schuldverhältnis (Vertrag) | Kläger | Anlage K1 (Werkvertrag v. 12.03.2022) | ✅ belegt | – |
| 2 | Pflichtverletzung (Nichtleistung) | Kläger | Mahnung Anlage K3; Zeuge Müller | ⚠️ streitig | Bekl. bestreitet Verzug; Zugang prüfen |
| 3 | Fristsetzung (§ 281 Abs. 1) | Kläger | Anlage K3 | ⚠️ Zugang bestritten | [LÜCKE: Rückschein fehlt → Aufgabe Zustellungsnachweis] |
| 4 | Vertretenmüssen (§ 280 Abs. 1 S. 2 BGB) | Schuldner (Umkehr) | – | ✅ vermutet | Bekl. muss Exkulpation vortragen |
| 5 | Schaden | Kläger | Rechnungen Anlage K5–K7 | ✅ belegt | – |
| 6 | Kausalität | Kläger | Gutachten (§ 286 ZPO) | ⚠️ offen | [LÜCKE: SV-Gutachten erforderlich] |

**Gesamtbewertung:** Mittel – Kernproblem: Nachweis des Zugangs der Fristsetzung und Kausalitätsbeleg durch Sachverständigengutachten.

## Risiken / typische Fehler

- **Beweislastumkehr übersehen:** Bei § 280 Abs. 1 S. 2 BGB liegt Entlastungspflicht beim Schuldner; nicht als Klägeraufgabe eintragen.
- **Lücken im Urkundenbeweis:** Vorlageanordnung nach § 142 ZPO ist kein Parteienrecht, sondern richterliches Ermessen; Antrag muss Anlass nennen (Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 142 Rn. 4).
- **Patentanspruch zu weit ausgelegt:** Merkmalsanalyse muss wortsinngemäß beginnen; Äquivalenz erst im zweiten Schritt (BGH – „Schneidmesser II").
- **Auskunfts-/Stufenklage nicht berücksichtigt:** Bei fehlender Kenntnis des Schadens kann Stufenklage (§ 254 ZPO) sinnvoll sein; Anspruchstabelle sollte Auskunftsstufe separat ausweisen.
