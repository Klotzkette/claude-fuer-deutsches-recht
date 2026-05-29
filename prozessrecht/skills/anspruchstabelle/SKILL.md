---
name: anspruchstabelle
description: "Anspruchstabelle für zivilprozessuales Mandat erstellen: alle Ansprüche und Gegenansprüche tabellarisch erfassen. Normen: §§ 253 261 ZPO. Prüfraster: Anspruchsgrundlage, Betrag, Verjaebrung, Beweisstatus. Output: Anspruchstabelle als Grundlage für Klageschrift oder Erwiderung. Abgrenzung: nicht Streitwertberechnung."
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

3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

4. **Lücken markieren:** Fehlende Belege und Beweismittel als **[LÜCKE]** mit Handlungsempfehlung (z. B. "Beauftragung Sachverständiger", "Auskunftsklage § 242 BGB / § 254 ZPO", "§ 142 ZPO Antrag auf Urkundenvorlage").

5. **Gegenargumente eintragen:** Bekannte oder antizipatierte Gegenargumente in Gegenargument-Spalte.

6. **Zusammenfassung:** Gesamtbewertung des Beweisrisikos (stark / mittel / schwach) mit Begründung.

### Modus Patent (`--patent`)

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Lücken und Risiken:** Unklare Merkmale, fehlende Dokumente zur angegriffenen Ausführungsform.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

Zivilrecht:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Patent:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
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
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- **Patentanspruch zu weit ausgelegt:** Merkmalsanalyse muss wortsinngemäß beginnen; Äquivalenz erst im zweiten Schritt (BGH – "Schneidmesser II").
- **Auskunfts-/Stufenklage nicht berücksichtigt:** Bei fehlender Kenntnis des Schadens kann Stufenklage (§ 254 ZPO) sinnvoll sein; Anspruchstabelle sollte Auskunftsstufe separat ausweisen.
