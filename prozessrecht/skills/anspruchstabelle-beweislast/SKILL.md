---
name: anspruchstabelle-beweislast
description: "Für Anspruchstabelle: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Beweislast- und Substantiierungsmatrix."
---

# Anspruchstabelle

## Zweck

Systematische Prüfung und Visualisierung aller Tatbestandsmerkmale eines zivilrechtlichen Anspruchs oder einer Einrede (z. B. Paragraf 280 Abs. 1, 3, Paragraf 281 BGB; Paragraf 823 Abs. 1 BGB; Paragraf 1 UWG) oder einer patentrechtlichen Verletzungsanalyse (Anspruchsmerkmal für Anspruchsmerkmal). Das Plugin erstellt eine Tabelle mit dem aktuellen Beweisstand, markiert Lücken und gibt Handlungsempfehlungen zur Schließung offener Punkte.

Zwei Modi:
- `--zivil`: Zivilrechtliche Ansprüche und Einreden (BGB, HGB, UWG, MarkenG etc.)
- `--patent`: Patentrechtliche Verletzungs- (Paragrafen 9 ff. PatG) oder Nichtigkeitsanalyse (Paragraf 22 PatG i. V. m. Paragrafen 1–5 PatG)

## Eingaben

- Aktives Mandat (Slug)
- Modus: `--zivil [Anspruchsnorm]` oder `--patent [--verletzung | --nichtigkeit] [Patentanspruch-Nr.]`
- Relevante Dokumente (Vertrag, Korrespondenz, Zeugenliste, Sachverständigengutachten, Patentschrift, angegriffene Ausführungsform)
- Aktueller Beweisstand (was liegt vor, was ist streitig)

## Ablauf

### Modus Zivilrecht (`--zivil`)

1. **Norm zerlegen:** Tatbestandsmerkmale des Anspruchs vollständig aufführen (z. B. Paragraf 280 Abs. 1 BGB: Schuldverhältnis, Pflichtverletzung, Vertretenmüssen, Schaden, Kausalität). Einreden und Einwendungen des Gegners separat tabellarisieren.

2. **Beweisstand erfassen:** Für jedes Element: belegt/unbelegt/streitig; vorhandene Beweismittel (Urkunde, Zeugenaussage, Sachverständigengutachten, Geständnisfiktion Paragraf 138 Abs. 3 ZPO, Augenschein Paragraf 371 ZPO) eintragen.

3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

4. **Lücken markieren:** Fehlende Belege und Beweismittel als **[LÜCKE]** mit Handlungsempfehlung (z. B. "Beauftragung Sachverständiger", "Auskunftsklage Paragraf 242 BGB / Paragraf 254 ZPO", "Paragraf 142 ZPO Antrag auf Urkundenvorlage").

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
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Patent:
- Mes, PatG, 5. Aufl. 2020, Paragraf 9 Rn. 22 ff.
- Schulte/Voß, PatG, 10. Aufl. 2017, Paragraf 9 Rn. 48 ff.

## Ausgabeformat

### Zivilrechtliche Anspruchstabelle

**Anspruch:** Schadensersatz wegen Pflichtverletzung (Paragrafen 280 Abs. 1, 3, 281 Abs. 1 BGB)

| Nr. | Tatbestandsmerkmal | Beweislast | Beweismittel (vorhanden) | Status | Lücke / Maßnahme |
|---|---|---|---|---|---|
| 1 | Schuldverhältnis (Vertrag) | Kläger | Anlage K1 (Werkvertrag v. 12.03.2022) | ✅ belegt | – |
| 2 | Pflichtverletzung (Nichtleistung) | Kläger | Mahnung Anlage K3; Zeuge Müller | ⚠️ streitig | Bekl. bestreitet Verzug; Zugang prüfen |
| 3 | Fristsetzung (Paragraf 281 Abs. 1) | Kläger | Anlage K3 | ⚠️ Zugang bestritten | [LÜCKE: Rückschein fehlt → Aufgabe Zustellungsnachweis] |
| 4 | Vertretenmüssen (Paragraf 280 Abs. 1 S. 2 BGB) | Schuldner (Umkehr) | – | ✅ vermutet | Bekl. muss Exkulpation vortragen |
| 5 | Schaden | Kläger | Rechnungen Anlage K5–K7 | ✅ belegt | – |
| 6 | Kausalität | Kläger | Gutachten (Paragraf 286 ZPO) | ⚠️ offen | [LÜCKE: SV-Gutachten erforderlich] |

**Gesamtbewertung:** Mittel – Kernproblem: Nachweis des Zugangs der Fristsetzung und Kausalitätsbeleg durch Sachverständigengutachten.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Risiken / typische Fehler

- **Beweislastumkehr übersehen:** Bei Paragraf 280 Abs. 1 S. 2 BGB liegt Entlastungspflicht beim Schuldner; nicht als Klägeraufgabe eintragen.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- **Patentanspruch zu weit ausgelegt:** Merkmalsanalyse muss wortsinngemäß beginnen; Äquivalenz erst im zweiten Schritt (BGH – "Schneidmesser II").
- **Auskunfts-/Stufenklage nicht berücksichtigt:** Bei fehlender Kenntnis des Schadens kann Stufenklage (Paragraf 254 ZPO) sinnvoll sein; Anspruchstabelle sollte Auskunftsstufe separat ausweisen.
