---
name: feature-risikobewertung
description: "Tiefgehende Risikobewertung für ein einzelnes Feature oder einen Produktbereich wenn der Launch-Review etwas gefunden hat das mehr als eine Tabellenzeile braucht. Strukturierte Analyse: was könnte schiefgehen, wie wahrscheinlich, wie schlimm, was mildert es. Verwenden wenn der Nutzer sagt „tiefer Einblick in dieses Risiko\", „Risikobewertung für [Feature]\", „was könnte schiefgehen mit\", oder wenn launch-pruefung eine neuartige Frage flaggt. Besonders einschlägig bei: UWG-Verstoßrisiken, DSGVO-Verletzung, DSA-Pflichten, KI-VO-Anforderungen, Verbraucherschutz nach BGB."
---

# Feature-Risikobewertung

## Mandat-Kontext

**Mandat-Kontext.** `## Mandate-Workspaces` in der praxisseitigen CLAUDE.md prüfen. Wenn `Aktiviert` `✗` ist (Standard für In-House-Nutzer), diesen Absatz überspringen. Wenn aktiviert und kein aktives Mandat, fragen: „Für welches Mandat ist das? `/produktrecht:produktrecht-mandat-arbeitsbereich switch <kürzel>` ausführen oder 'Praxisebene' sagen." Das aktive `mandat.md` für mandatsspezifischen Kontext laden. Ausgaben in den Mandat-Ordner schreiben. Niemals Dateien eines anderen Mandats lesen außer `Mandats-übergreifender Kontext` ist `ein`.

---

## Zweck

Der Launch-Review ist breit. Dies ist tief. Wenn eine einzelne Frage mehr als eine Tabellenzeile braucht – ein neuartiges KI-Feature, ein Produkt für Minderjährige, etwas das ein Behörde aktiv beobachtet – erstellt dieser Skill eine eigenständige Bewertung.

Nicht jeder Launch braucht eine. Die meisten nicht. Dies ist für die 10% wo „DSFA fertig, geshippt" nicht das richtige Prüfungsniveau ist.

## Eingaben

- Feature-Beschreibung oder PRD (eingefügt oder Tracker-Link)
- Anlass der Eskalation (was hat den Launch-Review ausgelöst dass dies eine tiefere Prüfung braucht)
- Anwendbare Jurisdiktionen und Nutzersegmente
- Bestehende Minderungsmaßnahmen die bereits umgesetzt sind

## Wann dies ausführen

- Launch-Review fand ein Muster das **nicht in der Kalibrierungstabelle ist** (neuartig)
- Launch-Review fand etwas in der **„blockiert normalerweise"**-Kategorie
- GC oder Unternehmensleitung fragte „was ist das Risiko hier" und möchte mehr als eine Einzeiler
- Das Feature liegt in einem Bereich mit **aktiver Regulierungsaufmerksamkeit** (KI/KI-VO, Minderjährige, biometrisch, Gesundheit, Dark Patterns nach § 5 UWG)
- Jemand außerhalb der Rechtsabteilung ist besorgt und eine strukturierte Antwort wäre hilfreich

Wenn keines davon zutrifft, reicht der Launch-Review. Keine Dokumente um der Dokumente willen erstellen.

## Ablauf

### 1. Was wird bewertet

Ein Absatz. Was das Feature tut, was neu daran ist, warum es zu einer vollständigen Bewertung eskaliert wurde.

### 2. Die Risiken

Für jedes einzelne Risiko (2–5, nicht 15):

```markdown
### Risiko [N]: [Kurzname]

**Szenario:** [Was eintreten müsste damit dies schiefgeht. Konkret –
nicht „Datenschutzverletzung" sondern „der Empfehlungsalgorithmus zeigt dem
Nutzer die sensible Kategorie-Interesse eines anderen wegen X."]

**Wer wird geschädigt:** [Nutzer? Das Unternehmen? Ein Dritter? Konkret.]

**Wie wahrscheinlich:** [Gering / Mittel / Hoch – mit Begründung. „Gering – würde
erfordern dass sowohl X als auch Y gleichzeitig scheitern." Nicht nur ein
Bauchgefühl.]

**Wie schlimm wenn es passiert:** [Gering / Mittel / Hoch – mit Begründung.
„Hoch – behördliches Bußgeld (bis 4% Jahresumsatz, Art. 83 DSGVO) + Abmahnwelle
+ Presseschaden" vs. „Gering – eine Verbraucherbeschwerde, kein tatsächlicher
Schaden."]

**Bestehende Minderungen:** [Was bereits Wahrscheinlichkeit oder Auswirkung
reduziert]

**Lücke:** [Was fehlt, falls vorhanden]

**Restrisiko:** [Nach bestehenden Minderungen – akzeptabel oder braucht mehr?]
```

### 3. Regulierungslandschaft (falls relevant)

Nur einbeziehen wenn eine Behörde sich aktiv für diesen Bereich interessiert. Falls ja:

- Welche Behörde (BaFin, BKartA, Datenschutzbehörde, Bundesnetzagentur), was haben sie kürzlich gesagt/getan
- Wie dieses Feature aus ihrer Sicht aussehen würde
- Ob wir lieber wollen dass sie davon von uns hören oder aus einer Überschrift

**Relevante deutsche Behörden und jüngste Prioritäten:**
- **BKartA:** Dark Patterns nach § 19a GWB, Daten-Tying, Marktbeherrschungsmissbrauch digitaler Unternehmen; vgl. Sektoruntersuchung Online-Werbung 2023
- **DSK / Datenschutzbehörden:** DSGVO-Konformität Tracking, Cookie-Banner (vgl. DSK-Beschluss Cookie II, 2021), KI-gestützte Profilbildung
- **BaFin:** Finanzprodukte, BNPL-Features, Zahlungsdienste
- **BZAW/Wettbewerbs-Verbände:** UWG-Abmahnungen; vgl. Abmahnstatistik UWG-Forum
- **EU-Kommission:** DSA-Durchsetzung (VLOP-Status), DMA-Gatekeeper-Compliance
- **EUAI-Behörde (AI Office):** KI-VO-Vollzug ab 2025/2026

### 4. Präzedenz (falls vorhanden)

Hat ein anderes Unternehmen etwas Ähnliches gemacht? Was passierte?

**Relevante Präzedenzfälle im deutschen Produktrecht:**
- *BGH, Urt. v. 24.07.2014 – I ZR 161/13 – „Kolumbus"* [Modellwissen – prüfen]: Irreführende Rabattwerbung ohne tatsächliche Preissenkung
- *OLG München, Urt. v. 08.04.2021 – 29 U 2091/20*: Cookie-Banner-Anforderungen
- *LG Berlin, Urt. v. 26.11.2020 – 16 O 341/15 – „Airbnb"*: AGB-Kontrolle, Transparenzgebot
- *BGH, Urt. v. 14.03.2017 – VI ZR 721/15 – Nutzerdaten*: Datenhaftung bei Plattformen

Vorrang nicht überschätzen. Regulierungsbehörden ändern Prioritäten; dass ein Unternehmen damit durchgekommen ist bedeutet nicht dass das nächste es auch tut.

### 5. Optionen

2–3 realistische Wege präsentieren:

```markdown
| Option | Beschreibung | Risikoreduzierung | Kosten |
|---|---|---|---|
| A: Wie geplant shippen | [aktueller Plan] | Keine | Keine |
| B: Mit [Minderung] shippen | [Änderung] | [wie viel] | [Entwicklungsaufwand, Timeline, UX] |
| C: [Komponente] nicht shippen | [Umfangskürzung] | [wie viel] | [Produktauswirkung] |
```

### 6. Empfehlung

Eine wählen. Erklären warum. Anerkennen was abgewogen wird.

```markdown
**Empfohlen: Option [X]**

[Warum. Welches Risiko verbleibt. Warum das akzeptabel ist. Wer es akzeptiert.]

**Wenn die Antwort „nicht meine Entscheidung" ist:** [Wer entscheidet, was sie wissen müssen]
```

## Kalibrierungscheck

Vor der Fertigstellung gegen `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` → Risikokalibrierung prüfen:

- Ist diese Risikobewertung auf *dieses Unternehmen* kalibriert, oder ist sie generisch?
- Ein Risiko das bei einem Unternehmen unter einem Bußgeldbescheid „Hoch" ist könnte bei einem das es nicht ist „Mittel" sein
- Die Bewertung sollte die tatsächliche Regulierungsposition, Streithistorie und den Risikoappetit im Praxisprofil widerspiegeln

## Besondere Prüfrahmen nach Rechtsgebiet

### UWG-Risiko (§§ 3, 5, 5a, 5b, 7 UWG)

Prüfen:
- Könnte das Feature Verbraucher über wesentliche Merkmale irren? (§ 5 UWG)
- Enthält das Feature Dark Patterns die Nutzerentscheidungen unlauter manipulieren? (§ 3 UWG; vgl. BGH, Urt. v. 06.06.2019 – I ZR 67/18 – „Influencer")
- Werden wesentliche Informationen verschwiegen? (§ 5a UWG)
- Werden Verbraucher unzumutbar belästigt? (§ 7 UWG: unerwünschte E-Mail, Telefonwerbung, Push-Nachrichten)
- Vergleichende Werbung: objektiv, kein Anschwärzen, Vergleich wesentlicher Merkmale? (§ 6 UWG)

Leitkommentare: Köhler/Bornkamm/Feddersen UWG, 42. Aufl. 2024, § 5 Rn. 1 ff.; Harte-Bavendamm/Henning-Bodewig UWG, 5. Aufl. 2021.

### DSGVO/TDDDG-Risiko

Prüfen:
- Neue Datenerhebung: Welche Rechtsgrundlage (Art. 6 DSGVO)? Einwilligung oder berechtigtes Interesse?
- Besondere Kategorien (Art. 9 DSGVO): Gesundheit, politische Meinung, sexuelle Orientierung – strenge Pflichten
- Profilbildung und automatisierte Entscheidungen: Art. 22 DSGVO wenn Entscheidungen automatisch und erheblich beeinträchtigend
- Cookies und Tracking: § 25 TDDDG (Einwilligung erforderlich für nicht-technisch-notwendige Cookies)
- Datenweitergabe an Dritte: AV-Vertrag (Art. 28 DSGVO), Drittlandtransfer (Art. 44 ff. DSGVO)
- Übergabe an: `/datenschutzrecht:anwendungsfall-triage [Feature]` wenn DSFA erforderlich

### DSA-Risiko (VO (EU) 2022/2065)

Relevant für Plattformen, Marktplätze, sehr große Online-Plattformen (VLOP):
- Art. 26: Werbung-Transparenz (Kennzeichnungspflicht für Werbung, keine Targeting auf Minderjährige)
- Art. 27: Empfehlungssysteme (transparente Parameter, Opt-out-Option)
- Art. 28: Schutz von Minderjährigen (keine Profil-Werbung für Personen unter 18)
- Art. 17–18: Beschwerde- und Abhilfemechanismen für illegale Inhalte

Relevant bei: Empfehlungsalgorithmen, Nutzer-Targeting, Moderationsentscheidungen, Werbeanzeigen.

### KI-VO-Risiko (VO (EU) 2024/1689)

**Risikoklassifizierung zuerst:**

| KI-Nutzung | Risikoklasse | Konsequenz |
|---|---|---|
| Biometrische Fernidentifikation | Verboten (ab 02.02.2025) | Nicht erlaubt |
| Social Scoring durch Behörden | Verboten | Nicht erlaubt |
| Emotionserkennung am Arbeitsplatz | Hochrisiko | Art. 9–15: DSFA, Register, CE |
| KI in kritischer Infrastruktur | Hochrisiko | Strenges Konformitätsregime |
| KI-Empfehlungssystem (nicht VLOP) | Begrenzt | Art. 50: Transparenzpflichten |
| Generative KI (GPAI) | GPAI-spezifisch | Art. 53: Urheberrechtsschutz, Transparenz |
| KI-Chatbot für Verbraucher | Begrenzt | Art. 50: Kennzeichnung als KI |

**Übergabe an:** `/ki-governance:anwendungsfall-triage [Feature]` wenn KI-Komponente erkannt.

### Verbraucherschutz BGB/BGB §§ 305 ff.

Prüfen:
- AGB-Klauseln: Einbeziehungsanforderungen (§§ 305, 305c BGB), überraschende Klauseln, Inhaltskontrolle (§§ 307–309 BGB)
- Fernabsatz: Widerrufsrecht (§§ 312g, 355 BGB), Widerrufsbelehrung (Muster-Widerrufsformular)
- Verbraucherverträge: wesentliche Informationen (Art. 246a EGBGB), Buttonlösung (§ 312j BGB)
- Gewährleistung: § 434 BGB (Produktmangel, Übereinstimmung mit öffentlichen Äußerungen inkl. Werbeaussagen)

## Übergaben

- **An KI-Governance:** Wenn der tiefe Einblick durch ein KI-Feature ausgelöst wurde – `/ki-governance:ki-folgenabschaetzung [Feature]` parallel oder sofort danach ausführen. Die Feature-Risikobewertung rahmt die Entscheidung; die KI-Folgenabschätzung dokumentiert das KI-System spezifisch. Sie sind keine Duplikate.
- **An Datenschutzrecht:** Wenn das Feature neue Datenerhebung oder -verarbeitung beinhaltet, `/datenschutzrecht:dsfa-erstellung [Feature]` ausführen.
- **An KI-Governance-Lieferantenprüfung:** Wenn das Feature einen neuen KI-Anbieter verwendet, `/ki-governance:ki-anbieter-prüfung [Lieferantenvertrag]` ausführen.

## Ausgabeformat

Eigenständiges Dokument, 2–4 Seiten. Arbeitsvermerk aus `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` `## Ausgaben` voranstellen.

Kein Foliensatz, kein Memo zur Akte – ein Entscheidungsdokument das jemand liest und dann entscheidet.

Speichern wo `~/.claude/plugins/config/claude-fuer-deutsches-recht/produktrecht/CLAUDE.md` → Launch-Review-Prozess sagt wohin Review-Dokumente gehen.

## Quellen und Zitierweise

Alle Zitate nach `../references/zitierweise.md` (BGH-Stil für Rechtsprechung, Kommentarzitate im Ernst/MüKo-Format).

**Pflicht-Beispielzitate für häufige Konstellationen:**

- BGH, Urt. v. 14.01.2016 – I ZR 65/14 – „Freunde finden", GRUR 2016, 946 Rn. 25 (Dark Patterns, Adressbuch-Import)
- BGH, Urt. v. 12.07.2018 – I ZR 74/17 – „Testsiegel auf der Verpackung", GRUR 2018, 1166 (Werbung mit Testergebnissen)
- EuGH, Urt. v. 01.10.2019 – C-673/17 – „Planet49", NJW 2019, 3503 (Cookie-Einwilligung)
- BGH, Urt. v. 28.05.2020 – I ZR 7/16 – „Cookie-Einwilligung II", NJW 2020, 2540
- Köhler, in: Köhler/Bornkamm/Feddersen UWG, 42. Aufl. 2024, § 5 Rn. 1.50 ff.

## Zitierprüfung

Wenn die Bewertung Fälle, Normen, Verordnungen oder Vollzugsmaßnahmen zitiert – insbesondere in der Regulierungslandschaft und Präzedenz-Abschnitten – wurden diese Zitate von einem KI-Modell generiert und wurden nicht gegen eine Primärquelle verifiziert. Vor Verwendung des Entscheidungsdokuments für Entscheidungsträger jeden Verweis gegen juris, beck-online oder die BGH-Website auf Richtigkeit, Status als geltendes Recht und aktuellen Vollzugsstand prüfen. Eine Risikobewertung die auf einem erfundenen Bußgeldbescheid aufbaut ist schlimmer als keine Bewertung.

## Risiken / typische Fehler

- **Überprüfung nicht ersetzen.** Diese Bewertung rahmt die Entscheidung – ein autorisierter Mensch wählt eine Option.
- **Kalibrierung vergessen.** Ein generisch „hohes" Risiko kann bei Ihrem Unternehmen „mittel" sein. Immer mit der Kalibrierungstabelle abgleichen.
- **Regulierungslandschaft ohne Forschung.** Keine Regulierungslandschaft aus Modellwissen ohne Quellenprüfung erstellen. Behörden-Positionen ändern sich.
- **DSGVO-Vollzugsfristen.** Meldepflicht Datenpanne nach Art. 33 DSGVO: 72 Stunden an zuständige Behörde. Diese Frist ist absolute Grenze.
- **Beweislast UWG.** Bei § 5 UWG: der Unternehmer muss die Richtigkeit einer Werbeaussage nachweisen, nicht der Verbraucher deren Unrichtigkeit (§ 5 Abs. 4 UWG für nachprüfbare Tatsachen).
