---
name: hinschg-whistleblower-interne-untersuchung
description: "Hinschg Whistleblower Interne Untersuchung im Plugin Arbeitsrecht: prüft konkret Arbeitnehmer hat einen internen Hinweis gegeben oder, Referenz-Skill, Rechtliche Prüfung einer ordentlichen oder, Prüft und entwirft eine Kündigungsschutzklage nach § 4 KSchG. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Hinschg Whistleblower Interne Untersuchung

## Arbeitsbereich

**Hinschg Whistleblower Interne Untersuchung** ordnet den Fall über die tragenden Prüfungslinien: Arbeitnehmer hat einen internen Hinweis gegeben oder, Referenz-Skill, Rechtliche Prüfung einer ordentlichen oder. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `hinschg-whistleblower-antwort` | Arbeitnehmer hat einen internen Hinweis gegeben oder Unternehmen muss internen Meldekanal einrichten oder Repressalie abwehren. Prüfraster HinSchG seit 2.7.2023 Umsetzung EU-Richtlinie 2019/1937. Pflicht interner Meldekanal ab 50 Beschaeftigte § 12 HinSchG. Meldungsschutz Repressalienverbot Beweislastumkehr § 36 HinSchG. Externe Meldung beim Bundesamt für Justiz § 19 ff. HinSchG. Geschützte Verstoesse § 2 HinSchG Schadensersatz § 37 HinSchG Bußgelder § 40 HinSchG bis 50000 EUR. Output Prüf-Memo Meldekanal-Konzept Repressalien-Abwehrschreiben. |
| `interne-untersuchung` | Referenz-Skill: gemeinsames Framework für arbeitsrechtliche interne Untersuchungen vom Eingang einer Beschwerde bis zum abschließenden Memo — vertrauliches Untersuchungsprotokoll, Dokumentenverarbeitung mit Relevanzprüfung, Quellendeckungs-Tracking, Abfragen gegen das Protokoll, Memo-Entwurf und Zielgruppen-Zusammenfassungen. Wird von /untersuchung-eroeffnen, /untersuchung-ergaenzen, /untersuchung-abfrage, /untersuchungs-memo und /untersuchungs-zusammenfassung geladen; nicht direkt aufzurufen. |
| `kuendigungs-pruefung` | Rechtliche Prüfung einer ordentlichen oder außerordentlichen Kündigung – KSchG (allgemeiner und besonderer Kündigungsschutz), § 102 BetrVG (Betriebsratsanhörung), §§ 622 und 626 BGB (Fristen und wichtiger Grund), Sozialauswahl § 1 Abs. 3 KSchG, Sonderkündigungsschutz (MuSchG, BEEG, SGB IX, § 15 KSchG). |
| `kuendigungsschutzklage` | Prüft und entwirft eine Kündigungsschutzklage nach § 4 KSchG. Lädt, wenn ein Arbeitnehmer eine ordentliche oder außerordentliche Kündigung anfechten will, die 3-Wochen-Frist droht oder ein Entwurf des Klageantrags, der Klagebegründung und der Sozialauswahl benötigt wird. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `hinschg-whistleblower-antwort`

**Fokus:** Arbeitnehmer hat einen internen Hinweis gegeben oder Unternehmen muss internen Meldekanal einrichten oder Repressalie abwehren. Prüfraster HinSchG seit 2.7.2023 Umsetzung EU-Richtlinie 2019/1937. Pflicht interner Meldekanal ab 50 Beschaeftigte § 12 HinSchG. Meldungsschutz Repressalienverbot Beweislastumkehr § 36 HinSchG. Externe Meldung beim Bundesamt für Justiz § 19 ff. HinSchG. Geschützte Verstoesse § 2 HinSchG Schadensersatz § 37 HinSchG Bußgelder § 40 HinSchG bis 50000 EUR. Output Prüf-Memo Meldekanal-Konzept Repressalien-Abwehrschreiben.

### HinSchG — Hinweisgeberschutz-Compliance und -Verteidigung

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `HinSchG — Hinweisgeberschutz-Compliance und -Verteidigung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage zu Beginn

1. Ist der Mandant **Hinweisgeber** (schutzsuchend) oder **Arbeitgeber** (Pflichten/Verteidigung)?
2. Wie viele Beschäftigte hat das Unternehmen? (Schwellenwert: 50 für Meldekanal-Pflicht)
3. Welcher Verstoß wird gemeldet? (Straftat / Unionsrechtsverstoß / sonstiger HinSchG-Verstoß)
4. Welcher Kanal wird genutzt? (intern / BfJ extern / sektorale Aufsicht / Öffentlichkeit)
5. Liegt bereits eine Repressalie vor? (Kündigung / Versetzung / Disziplinar nach Meldung)

## Zentrale Normen

- §§ 1, 2 HinSchG — Anwendungsbereich, geschützte Verstöße
- § 7 HinSchG — Wahlrecht: interner vs. externer Kanal
- §§ 12, 16-18 HinSchG — Pflicht zum Meldekanal, Verfahrensregeln (7 Tage Eingang / 3 Monate Rückmeldung)
- § 33 HinSchG — Repressalienverbot (Kündigung, Versetzung, Disziplinar, Bonus-Streichung)
- § 36 HinSchG — Beweislastumkehr bei Repressalien-Indizien
- § 37 HinSchG — Schadensersatzanspruch (materielle und immaterielle Schäden)
- § 40 HinSchG — Bußgelder bis 50.000 Euro je Verstoß
- EU-RL 2019/1937 — Whistleblower-Richtlinie (Umsetzung)

## Aktuelle Rechtsprechung (Stand Mai 2026)

Das HinSchG ist seit 02.07.2023 in Kraft; eine veroeffentlichte BAG-Leitentscheidung zur Beweislastumkehr (§ 36 HinSchG) ist zum Stand Mai 2026 ueber dejure.org/openjur.de nicht mit offener Quelle verifizierbar.

- ArbG Braunschweig, Urteil vom 24.06.2025 - 6 Ca 303/24: § 36 Abs. 2 Satz 2 HinSchG (Beweislastumkehr) gilt nicht auf der Rechtsfolgenseite; Kausalitaet eines konkret behaupteten Schadens ist vom Anspruchsteller zu belegen. Vorgesetzte sind nicht automatisch interne Meldestelle. Hinweisgeber muss substantiiert darlegen, wann, wo und welche konkrete Meldung erfolgte. Quelle: Hensche Arbeitsrecht (vor Schriftsatzverwendung Volltext ueber offene Quelle verifizieren).
- Bei Verwendung im Schriftsatz: erstinstanzliche Entscheidungen sind nicht bindend, neuere LAG/BAG-Rechtsprechung pruefen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Seit 2.7.2023 ist das HinSchG in Kraft (Umsetzung EU-RL 2019/1937). Dieses Skill bedient zwei Konstellationen: Mandant ist Beschäftigter (Whistleblower-Schutz) oder Arbeitgeber (Meldekanal-Pflicht und Repressalien-Verteidigung).

## Eingaben

- Konstellation (Beschäftigter / Arbeitgeber)
- Beschäftigten-Zahl des Arbeitgebers (Schwellenwerte)
- Meldung-Inhalt (welcher Verstoß?)
- Bisheriger Schriftwechsel
- Folge-Maßnahmen des Arbeitgebers (bei Beschäftigten-Konstellation)
- Kanal-Struktur (intern extern öffentlich)

## Konstellation A — Mandant ist Whistleblower

### Schritt A1 — Anwendungsbereich § 1 HinSchG

- **Schutz vor Repressalien** bei Meldung Offenlegung von Verstößen
- Bezug auf berufliches Umfeld
- Schutz erstreckt sich auf Beschäftigte, Selbstständige, Anteilseigner, Mitglieder von Verwaltungs-, Leitungs- oder Aufsichtsorganen, Praktikanten, Bewerber, Ex-Beschäftigte

### Schritt A2 — Geschützte Verstöße § 2 HinSchG

- **Straftaten** und **bestimmte Ordnungswidrigkeiten** (bei Schutz Leben Gesundheit oder Mitarbeiter-Rechte)
- **Verstöße gegen direkt anwendbares Unionsrecht** in bezeichneten Bereichen:
 - Finanzdienstleistungen
 - Geldwäsche
 - Produkt-Sicherheit
 - Verkehr
 - Umwelt
 - Strahlenschutz
 - Lebensmittel- und Futtermittel-Sicherheit
 - Tiergesundheit
 - Verbraucherschutz
 - Datenschutz und IT-Sicherheit
 - öffentliche Vergabe
 - bestimmte Steuer-Vorschriften
- **Verstösse die finanzielle EU-Interessen schädigen**
- **Verstösse gegen Wettbewerbs- und Beihilferecht**

### Schritt A3 — Meldewege § 7 HinSchG

#### Wahlrecht zwischen internem und externem Kanal

- **Intern** beim Arbeitgeber gemäß § 12 ff.
- **Extern** BfJ § 19 ff. oder sektorale Aufsicht (BaFin, BKartA)
- **Öffentlichkeit** § 32 nur bei strikten Voraussetzungen (keine Reaktion frühere Meldungen, unmittelbare Gefahr, Vergeltungs-Gefahr, Schaden für Allgemeinheit)

#### Empfehlung Mandant

- **Erst intern** wenn praktikabel — höhere Heilungs-Chance
- **Bei Vertrauensverlust intern** sofort extern
- **Öffentlichkeit nur als ultima ratio**

### Schritt A4 — Repressalien-Schutz § 33 HinSchG

#### Verbot Vergeltungs-Maßnahmen

- Kündigung Versetzung Disziplinar Bonus-Streichung Mobbing
- Auch nach Beschäftigungs-Ende (Referenz-Verweigerung)
- Auch im Bewerbungs-Prozess

#### Beweislast-Umkehr § 36 HinSchG

- Bei nachweis Repressalien-Indizien — Arbeitgeber muss widerlegen
- Bei Meldung plus zeitnahe Maßnahme — Vermutung

### Schritt A5 — Schadensersatz § 37 HinSchG

- **Materielle Schäden** Verdienst-Ausfall
- **Immaterielle Schäden** Schmerzensgeld
- BAG-Linien zur Bemessung

### Schritt A6 — Strafanzeige

- Bei zugleich Straftatbestand-Verdacht
- Parallele Anzeige bei StA
- Anonyme Möglichkeit

## Konstellation B — Mandant ist Arbeitgeber

### Schritt B1 — Pflicht zur Errichtung Meldekanal § 12 HinSchG

| Beschäftigten-Zahl | Pflicht |
|---|---|
| Bis 49 | Keine Errichtungs-Pflicht (außer Sektor-Sondernormen WpHG GwG etc.) |
| 50 bis 249 | Pflicht — Konzern-Lösung möglich (BAG offen) |
| Ab 250 | Pflicht — Einzelkanal pro Gesellschaft empfohlen |

#### Inhalts-Anforderungen Meldekanal § 16-18 HinSchG

- **Eingang** bestätigt binnen sieben Tagen
- **Rückmeldung** binnen drei Monaten zu Folge-Maßnahmen
- **Vertraulichkeit** der Hinweisgeber-Identität § 8 HinSchG
- **Schriftlich mündlich persönlich** Wahl-Möglichkeit § 16 Abs. 3 HinSchG
- **Anonyme Meldungen** Bearbeitung empfohlen (keine Pflicht aber sinnvoll)
- **Geschultes Personal** § 15 HinSchG

#### Externer Kanal-Anbieter

- **Auslagerung möglich** § 14 HinSchG
- AVV nach Art. 28 DSGVO
- Vertrauliche Hinweisgeber-Daten geschützt

### Schritt B2 — Verfahren bei Meldung

#### Verfahrens-Schritte § 17 HinSchG

1. Eingangs-Bestätigung sieben Tage
2. Plausibilitäts-Prüfung
3. Untersuchungs-Maßnahmen
4. Rückmeldung Hinweisgeber binnen drei Monaten
5. Folge-Maßnahmen bei begründetem Verdacht
6. Abschluss-Dokumentation

#### Vertraulichkeits-Schutz

- Hinweisgeber-Identität geheim — auch innerhalb des Untersuchungs-Teams
- Ausnahme nur bei Pflicht-Offenlegung gegenüber Strafverfolgungs-Behörden

### Schritt B3 — Repressalien-Vorwurf-Verteidigung

#### Bei Kündigung nach Meldung — Risiko-Konstellation

- Beweislast-Umkehr § 36 HinSchG
- Arbeitgeber muss Sachgrund unabhängig von Meldung dartun
- Sorgfältige Begründungs-Dokumentation
- Trennung der Verantwortlichkeits-Ebene

#### Strategie

- **Zeitabstand** zwischen Meldung und Maßnahme
- **Sachgrund-Dokumentation** vorher schon
- **Unabhängige Entscheider** ohne Kenntnis Meldung
- **Externe Compliance-Audit** zur Sachgrund-Sicherheit

### Schritt B4 — Bußgeld-Risiken § 40 HinSchG

- **EUR 50.000** bei Nicht-Errichtung Meldekanal
- **EUR 50.000** bei Behinderung Meldung
- **EUR 50.000** bei Repressalien
- **EUR 20.000** bei Verletzung Vertraulichkeits-Pflicht

## Schritt 1 (übergreifend) — Schnittstelle DSGVO

### Datenschutz im Meldekanal

- Art. 6 DSGVO Rechtsgrundlage Art. 6 Abs. 1 lit. c (rechtliche Verpflichtung HinSchG)
- Art. 30 DSGVO Verarbeitungs-Verzeichnis-Eintrag
- Art. 35 DSGVO DSFA empfohlen bei umfangreichem Kanal

### EU-Vorgaben

- EDSA Stellungnahme 2/2022 zum Whistleblowing
- Spezifische Erwägungs-Gründe zu Hinweisgeber-Schutz

## Schritt 2 (übergreifend) — Verzahnung Kündigungs-Konstellation

### Wenn Kündigung nach Meldung

- Kündigungsschutz-Klage drei-Wochen-Frist § 4 KSchG
- HinSchG-Repressalien-Vorwurf zusätzlich
- Sozialgerichts-Bezug bei ALG-Sperrzeit

### Mit Aufhebungsvertrag

- Bei Verdacht Vergeltungs-Aufhebungsvertrag
- Anfechtbarkeit § 123 BGB Drohung
- Sperrzeit-Risiko § 159 SGB III

## Schritt 3 — Strategische Empfehlungen

### Whistleblower-Mandant

- **Sorgfältige Dokumentation** vor und nach Meldung
- **Erste Meldung intern** wenn praktikabel
- **Externe Meldung** bei Vertrauensverlust
- **Anwalt frühzeitig** für Schutz-Beratung
- **Beweissicherung** Repressalien

### Arbeitgeber-Mandant

- **Meldekanal sofort errichten** (Pflicht)
- **Konzern-Lösung** prüfen (50-249 Beschäftigte)
- **Geschultes Personal** für Bearbeitung
- **Verfahrens-Handbuch** intern
- **Externe Beratung** bei kritischer Meldung — Vermeidung Eigen-Befangenheit
- **Strikte Vertraulichkeit** sicherstellen

## Schritt 4 — Spezielle Sektoren

### Finanzdienstleistungen

- **WpHG** § 23 Meldepflicht zusätzlich
- **BaFin-Hinweisgeber-System** spezifisch
- **Kreditinstitute § 25a KWG**

### Gesellschaftsrecht / Aufsichtsrat

- Bei Compliance-Pflichtverletzungen Geschäftsführer-/Vorstands-Haftung
- D&O-Versicherung-Bezug

### Öffentliche Verwaltung

- Sondernormen Beamten-Verhältnis

## Schritt 5 — Mustervorlagen

### Meldung intern (Whistleblower-Sicht)

```
An die interne Hinweisgebermeldestelle der [Unternehmen]

Meldung gem. § 7 i. V. m. § 16 HinSchG vom [Datum]
(§ 17 HinSchG regelt das nachfolgende
Meldestellen-Verfahren, nicht die Meldung selbst)

Hiermit melde ich folgenden Sachverhalt:

[Konkrete Sachverhalts-Schilderung mit Datum Ort Beteiligten
Beweismitteln]

Diese Meldung erfolgt unter Berufung auf das
Hinweisgeberschutzgesetz. Ich beanspruche den
Vertraulichkeitsschutz nach § 8 HinSchG und den
Repressalienschutz nach § 33 HinSchG.

[Optional: Anonyme Bearbeitung ja/nein]
```

### Bestätigung Eingang (Arbeitgeber-Sicht)

```
Eingangsbestätigung gemäß § 17 Abs. 1 Nr. 1 HinSchG

Ihre Meldung vom [Datum] ist bei uns am [Datum]
eingegangen. Wir werden den Sachverhalt prüfen
und Ihnen binnen drei Monaten gemäß § 17 Abs. 1
Nr. 4 HinSchG Rückmeldung über Folge-Maßnahmen
geben.

Ihre Identität wird gemäß § 8 HinSchG vertraulich
behandelt.

Bei Rückfragen wenden Sie sich bitte an
[Kontakt-Person].
```

## Ausgabe

- `hinschg-{az}.md` mit Konstellations-Analyse
- Schriftsätze (Meldung Eingangs-Bestätigung Rückmeldung)
- Bei Whistleblower: Schutz-Strategie und Beweis-Sicherung
- Bei Arbeitgeber: Meldekanal-Aufbau Verfahrens-Handbuch
- Bei Kündigungs-Konstellation: Schnittstelle KSchG-Klage
- Frist im Fristenbuch (drei Monate Rückmeldung sieben Tage Eingangs-Bestätigung)

## Quellen

- HinSchG §§ 1 2 8 12 15 16 17 19 32 33 36 37 40
- EU-RL 2019/1937
- DSGVO Art. 6 30 35
- EDSA Stellungnahme 2/2022
- BAG zu Repressalien-Beweislast
- BfJ-Hinweisgeber-Stelle
- Garden/Hinrichs HinSchG

## 2. `interne-untersuchung`

**Fokus:** Referenz-Skill: gemeinsames Framework für arbeitsrechtliche interne Untersuchungen vom Eingang einer Beschwerde bis zum abschließenden Memo — vertrauliches Untersuchungsprotokoll, Dokumentenverarbeitung mit Relevanzprüfung, Quellendeckungs-Tracking, Abfragen gegen das Protokoll, Memo-Entwurf und Zielgruppen-Zusammenfassungen. Wird von /untersuchung-eroeffnen, /untersuchung-ergaenzen, /untersuchung-abfrage, /untersuchungs-memo und /untersuchungs-zusammenfassung geladen; nicht direkt aufzurufen.

### Interne Untersuchung — Referenz-Skill (Arbeitsrecht)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Interne Untersuchung — Referenz-Skill (Arbeitsrecht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Interne Untersuchungen scheitern auf zwei Wegen: fehlende Quellenabdeckung
(Erkenntnisquellen, die nie erhoben wurden) und fehlende Synthese (Erkenntnisse,
die erhoben wurden, aber nie verknüpft wurden). Diese Skill adressiert beide
Schwachstellen — sie verfolgt, was erhoben wurde und was nicht, verarbeitet
Dokumentenmassen zur Identifikation des Wesentlichen ohne den Anwalt zu
überwältigen, und führt ein strukturiertes Protokoll, das jederzeit zu einem
vertraulichen Memo verdichtet werden kann.

## Vertraulichkeit und Datenschutz

> **Vertraulichkeit.** Alle durch diese Skill erstellten Dateien — Protokolleinträge,
> Memo-Entwürfe, Zielgruppen-Zusammenfassungen, Dokumentennotizen — teilen den
> Vertraulichkeitsstatus der zugrundeliegenden Untersuchung. Eine Weitergabe über
> den autorisierten Kreis hinaus (an nicht beteiligte Dritte, HR ohne ausreichende
> Einschränkung, die Unternehmensseite ohne rechtliche Steuerung) kann den
> Schutzcharakter der Unterlagen gefährden. Alle Dateien dort aufbewahren, wo
> vertrauliche Unterlagen gelagert werden, und jede Weitergabe bewusst entscheiden.

**§ 26 BDSG — Beschäftigtendatenschutz**: Die Verarbeitung personenbezogener
Beschäftigtendaten im Rahmen interner Untersuchungen ist nur zulässig, wenn
sie zur Aufdeckung von Straftaten oder schwerwiegenden Pflichtverletzungen
erforderlich ist und das schutzwürdige Interesse der betroffenen Arbeitnehmer
nicht überwiegt. Verhältnismäßigkeit ist bei jedem Schritt zu prüfen.

**Mitbestimmung § 87 Abs. 1 Nr. 6 BetrVG**: Der Einsatz technischer
Überwachungseinrichtungen (z. B. E-Mail-Auswertung, IT-Forensik) unterliegt
dem Mitbestimmungsrecht des Betriebsrats. Bevor Kommunikationsauswertungen
vorgenommen werden, ist die Zustimmung des Betriebsrats oder eine
Betriebsvereinbarung zur Unternehmensführung erforderlich.

**Detektivkosten**: Kosten für externe Ermittler sind nach der
BAG-Rechtsprechung nur unter engen Voraussetzungen als Schadensersatz
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 26 BDSG: Datenverarbeitung für Zwecke des Beschäftigungsverhältnisses;
 Verarbeitung zur Aufdeckung von Straftaten; Verhältnismäßigkeit
- Art. 5, 6 DSGVO: Rechtmäßigkeit der Verarbeitung; berechtigtes Interesse
 als Verarbeitungsgrundlage
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen
 Überwachungseinrichtungen
- § 32 BDSG a.F. / § 26 BDSG n.F.: Kontinuität der Rspr. zur
 Beschäftigtendatenverarbeitung
- § 611a BGB: Arbeitnehmereigenschaft; Mitwirkungspflichten im
 Arbeitsverhältnis
- § 241 Abs. 2 BGB: Nebenpflichten, insbesondere Auskunftspflicht des
 Arbeitnehmers im Rahmen des Arbeitsverhältnisses
- §§ 626, 314 BGB: Außerordentliche Kündigung bei schwerwiegenden
 Pflichtverletzungen; Verdachtskündigung

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Verdachtskündigung — Voraussetzungen: dringender Tatverdacht auf Basis
 objektiver Umstände, Verhältnismäßigkeit, vorherige Anhörung des
 Arbeitnehmers als zwingende Wirksamkeitsvoraussetzung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Erstattungsfähigkeit von Detektivkosten — nur soweit konkrete Verdachtslage
 bei Beauftragung bestand und Verhältnismäßigkeit gewahrt ist
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Verwertungsverbot rechtswidrig erlangter Erkenntnisse — heimliche
 Videoüberwachung ohne Mitbestimmung des Betriebsrats; Beweisverwertungsverbot
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Anhörung vor Verdachtskündigung — inhaltliche Mindestanforderungen und
 Fehlerfolgen bei fehlerhafter Anhörung

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- § 626 BGB: Zwei-Wochen-Frist, Verdachtskündigung und Anhörung nur mit verifizierter BAG-Rechtsprechung oder Nutzerquelle vertiefen.
- Beschäftigtendatenschutz: § 26 BDSG, Art. 5 und 6 DSGVO; Fachliteratur nur mit Nutzerquelle oder verifiziertem Live-Zugriff.
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen Überwachungseinrichtungen; Rechtsprechung nur frei verifiziert zitieren.
- AGG: §§ 12, 15, 22 AGG anhand Gesetz, Nutzerquelle und frei verifizierter Rechtsprechung prüfen.

---

## Modus 1: Neue Untersuchung eröffnen

Ausgelöst durch `/arbeitsrecht:untersuchung-eroeffnen` oder
"Untersuchung eröffnen" / "Untersuchung einleiten wegen".

### Schritt 1 — Sachverhaltserfassung

Frage folgende Punkte in einem einzigen Block ab:

> Zur Eröffnung des Untersuchungsprotokolls werden folgende Angaben benötigt:
>
> **Die Sache**
> - Was ist der Vorwurf oder die Besorgnis in eigenen Worten?
> - Wer ist Beschwerdeführer/in (oder welches Ereignis hat die Untersuchung
> ausgelöst — Beschwerde, Hinweis, Revision, Vorgesetztenwahrnehmung)?
> - Wer ist die beschuldigte oder in Frage stehende Person?
> - Welcher ungefähre Zeitraum soll untersucht werden?
> - Ist die Untersuchung anwaltsgeleitet? (Wenn ja: erhöhter Schutz
> der Arbeitsergebnisse. Wenn nein: Schutzstatus vor Beginn klären.)
>
> **Art der Untersuchung** (bestimmt die passende Quellencheckliste)
> - HR: Belästigung / Diskriminierung / Benachteiligung (AGG)
> - Finanzen: Spesenmanipulation / Beschaffungsunregelmäßigkeiten / Untreue
> - Führungskraft: Interessenkonflikt / unzulässige Beziehungen /
> Governance-Verstöße
> - Hinweisgeber: Vergeltung gegen geschützte Tätigkeit (§§ 34, 36 HinSchG)
> - Sonstiges: kurz beschreiben
>
> **Vertretung und Betriebsrat**
> - Ist die beschuldigte Person, die beschwerdeführende Person oder ein
> erwarteter Zeuge durch einen Betriebsrat vertreten oder durch Tarifvertrag
> erfasst? (Wenn ja: Informationsrecht des Betriebsrats nach § 102 BetrVG
> bei etwaiger Kündigung beachten; kein eigenständiges Teilnahmerecht an
> Investigativgesprächen, aber § 82 Abs. 2 BetrVG: Arbeitnehmer darf
> Betriebsratsmitglied zur Besprechung über Beschwerde hinzuziehen)
> - Ist die Gesellschaft ein öffentlich-rechtlicher Arbeitgeber (Behörde,
> Hochschule, Staatsunternehmen)? (Wenn ja: Besonderheiten des öffentlichen
> Dienstrechts, ggf. Personalvertretungsgesetz statt BetrVG prüfen)

Wenn Betriebsratsteilnahme-Frage aufgeworfen wird: § 82 Abs. 2 BetrVG,
§ 84 BetrVG (Beschwerderecht), § 85 BetrVG (Behandlung von Beschwerden)
recherchieren, bevor Gespräche geführt werden.

### Schritt 2 — Verzeichnis und Dateien anlegen

Erstelle folgende Dateien:

`investigation-[slug]/log.yaml`:

```yaml
### VERTRAULICH — INTERNE UNTERSUCHUNG — [Datum]
sache: "[Sachbezeichnung]"
sache_slug: "[slug]"
eroeffnet: "[ISO-Datum]"
anwaltsgeleitet: [true/false]
vorwurf: "[Sachverhaltsdarstellung in eigenen Worten]"
beschwerdefuehrer: "[Name/Funktion oder anonym]"
beschuldigter: "[Name/Funktion]"
tatverdachtszeitraum: "[ungefähre Daten]"
untersuchungsart: "[HR/Finanzen/Fuehrungskraft/Hinweisgeber/Sonstiges]"
status: offen
zuletzt_aktualisiert: "[ISO-Datum]"

fragen:
 - "[Frage 1 — aus dem Vorwurf abgeleitet, z. B. 'Liegt eine unzulässige
 Benachteiligung nach § 3 AGG vor?']"
 - "[Frage 2 falls zutreffend]"

eintraege: []

beweisluecken: []
```

`investigation-[slug]/quellen-checkliste.yaml`:
Wird aus der Untersuchungsart generiert — siehe Checklisten-Vorlagen unten.

`investigation-[slug]/dokumente-geprueft.yaml`:

```yaml
### VERTRAULICH — INTERNE UNTERSUCHUNG — [Datum]
sache: "[Sachbezeichnung]"
gesamt_geprueft: 0
gesamt_relevant: 0
zuletzt_aktualisiert: "[ISO-Datum]"
dokumente: []
```

### Schritt 3 — Quellencheckliste

Erstelle die passende Checkliste je nach Untersuchungsart und lege sie dem
Anwalt vor: "Passt diese Checkliste zu Ihrer Sache? Bitte melden Sie, welche
Punkte nicht anwendbar sind (werden als N/A markiert) und ob weitere
Quellen hinzukommen."

**HR-Untersuchung (Belästigung/Diskriminierung/Benachteiligung AGG):**
```yaml
quellen:
 - id: 1
 quelle: "Anhörung Beschwerdeführer/in"
 status: offen
 notizen: ""
 - id: 2
 quelle: "Anhörung Beschuldigte/r"
 status: offen
 notizen: ""
 - id: 3
 quelle: "Zeugenbefragungen — identifizieren aus Schilderungen beider Seiten"
 status: offen
 notizen: ""
 - id: 4
 quelle: "E-Mail-/Kommunikationsauswertung — Beteiligte, relevanter Zeitraum
 (§ 87 Abs. 1 Nr. 6 BetrVG beachten: Mitbestimmung Betriebsrat)"
 status: offen
 notizen: ""
 - id: 5
 quelle: "Personalakte Beschuldigte/r — Leistungsbeurteilungen, frühere
 Beschwerden, Disziplinarmaßnahmen"
 status: offen
 notizen: ""
 - id: 6
 quelle: "Frühere Beschwerden gegen Beschuldigte/n im HR-System"
 status: offen
 notizen: ""
 - id: 7
 quelle: "Vergleichspersonenanalyse — wie wurden ähnliche Fälle behandelt"
 status: offen
 notizen: ""
 - id: 8
 quelle: "Einschlägige Richtlinien — AGG-Richtlinie, Verhaltenskodex,
 Beschwerdeverfahren (Version zum Tatzeitpunkt)"
 status: offen
 notizen: ""
 - id: 9
 quelle: "Organigramm und Berichtslinien zum Tatzeitpunkt"
 status: offen
 notizen: ""
 - id: 10
 quelle: "Kalender / Terminvermerke — Besprechungen oder Ereignisse,
 die in Schilderungen erwähnt wurden"
 status: offen
 notizen: ""
 - id: 11
 quelle: "Dokumentation der Anhörungshinweise (§ 82 Abs. 2 BetrVG /
 Hinweis auf Recht zur Hinzuziehung eines BR-Mitglieds)"
 status: offen
 notizen: ""
```

**Finanzuntersuchung:**
```yaml
quellen:
 - id: 1
 quelle: "Spesenabrechnungen — betroffene Person, relevanter Zeitraum"
 status: offen
 notizen: ""
 - id: 2
 quelle: "Genehmigungsunterlagen — wer hat Ausgaben oder Transaktionen
 genehmigt"
 status: offen
 notizen: ""
 - id: 3
 quelle: "Lieferanten-/Auftragnehmerakte — Verträge, Rechnungen, Zahlungsbelege"
 status: offen
 notizen: ""
 - id: 4
 quelle: "Finanzsystem-Auswertungen — Kreditoren, Hauptbuch, relevante Konten"
 status: offen
 notizen: ""
 - id: 5
 quelle: "E-Mail-/Kommunikationsauswertung — betroffene Person, Genehmiger,
 Gegenparteien (§ 87 Abs. 1 Nr. 6 BetrVG beachten)"
 status: offen
 notizen: ""
 - id: 6
 quelle: "Anhörung der betroffenen Person"
 status: offen
 notizen: ""
 - id: 7
 quelle: "Anhörung Genehmiger"
 status: offen
 notizen: ""
 - id: 8
 quelle: "Anhörung Lieferanten / Auftragnehmer (soweit zugänglich)"
 status: offen
 notizen: ""
 - id: 9
 quelle: "Audit-Logs — Systemzugriffe für relevante Konten/Systeme"
 status: offen
 notizen: ""
 - id: 10
 quelle: "Frühere Prüfungen oder Reviews für den relevanten Zeitraum"
 status: offen
 notizen: ""
```

**Untersuchung Führungskraft (Interessenkonflikt/Governance):**
```yaml
quellen:
 - id: 1
 quelle: "Anhörung betroffene Führungskraft"
 status: offen
 notizen: ""
 - id: 2
 quelle: "Aufsichtsrats-/Gesellschafterbeschlüsse — relevante Resolutionen,
 Protokolle, Genehmigungen"
 status: offen
 notizen: ""
 - id: 3
 quelle: "Anstellungsvertrag und Änderungen / Nachträge"
 status: offen
 notizen: ""
 - id: 4
 quelle: "Beteiligungsunterlagen — Optionen, Übertragungen, Unverfallbarkeit"
 status: offen
 notizen: ""
 - id: 5
 quelle: "Spesenabrechnungen und Genehmigungsunterlagen"
 status: offen
 notizen: ""
 - id: 6
 quelle: "E-Mail-/Kommunikationsauswertung — betroffene Person, relevante
 Gegenparteien (§ 87 Abs. 1 Nr. 6 BetrVG beachten)"
 status: offen
 notizen: ""
 - id: 7
 quelle: "Interessenkonflikt-Erklärungen (oder Fehlen davon)"
 status: offen
 notizen: ""
 - id: 8
 quelle: "Unterlagen zu Nebentätigkeiten"
 status: offen
 notizen: ""
 - id: 9
 quelle: "Zeugenbefragungen — direkte Mitarbeiter, Kollegen, AR-Mitglieder"
 status: offen
 notizen: ""
 - id: 10
 quelle: "Frühere Beschwerden oder Hinweise auf betroffene Person"
 status: offen
 notizen: ""
```

**Hinweisgeberuntersuchung (HinSchG / Retaliation):**
```yaml
quellen:
 - id: 1
 quelle: "Anhörung hinweisgebende Person"
 status: offen
 notizen: ""
 - id: 2
 quelle: "Ursprüngliche Meldung oder Hinweis — schriftlich, soweit vorhanden"
 status: offen
 notizen: ""
 - id: 3
 quelle: "Unterlagen zum gemeldeten Sachverhalt (der eigentliche Hinweis)"
 status: offen
 notizen: ""
 - id: 4
 quelle: "Unterlagen zu nachteiligen Maßnahmen gegenüber hinweisgebender
 Person nach der Meldung (§§ 36, 37 HinSchG)"
 status: offen
 notizen: ""
 - id: 5
 quelle: "Anhörung Entscheidungsträger der nachteiligen Maßnahme"
 status: offen
 notizen: ""
 - id: 6
 quelle: "Vergleichspersonenanalyse — Behandlung vergleichbarer Personen
 ohne Meldetätigkeit"
 status: offen
 notizen: ""
 - id: 7
 quelle: "E-Mail-/Kommunikationsauswertung — Entscheidungsträger,
 relevanter Zeitraum"
 status: offen
 notizen: ""
 - id: 8
 quelle: "Zeitliche Nähe: Meldetätigkeit zu nachteiliger Maßnahme
 (§ 36 Abs. 2 HinSchG: Beweislastumkehr)"
 status: offen
 notizen: ""
 - id: 9
 quelle: "Anhörung Beschuldigte/r / Entscheidungsträger"
 status: offen
 notizen: ""
```

---

## Modus 2: Daten hinzufügen

Ausgelöst durch `/arbeitsrecht:untersuchung-ergänzen`.

### Schritt 1 — Sache identifizieren

Falls mehrere Untersuchungsordner existieren: Frage, zu welcher Sache die
Daten gehören. Bei nur einer Sache: direkt fortfahren.

### Schritt 2 — Datenart identifizieren

Frage (sofern nicht aus dem Kontext klar):
- Befragungsnotizen (von wem?)
- Dokumentenpaket (E-Mails, Akten, Dateien)
- Anwaltsnotizen oder Beobachtungen
- Bestätigung eines Anhörungshinweises

**§ 26 BDSG-Verhältnismäßigkeitsprüfung**: Bei Dokumentenpaketen stets prüfen,
ob die Verarbeitung der enthaltenen Beschäftigtendaten zur Aufklärung des
Vorwurfs erforderlich und verhältnismäßig ist.

### Schritt 3 — Auswahlkriterien für Dokumente

Für jedes Dokumentenpaket gelten folgende Auswahlkriterien. Ein Dokument
wird markiert, wenn es mindestens eines erfüllt. Die Kriterien sind bewusst
etwas weit gefasst — ein False Positive ist besser als ein übersehener
relevanter Fund.

**Auswahlkriterien:**
1. Enthält den Namen einer Untersuchungsbeteiligten (Beschwerdeführer/in,
 Beschuldigte/r, benannte Zeugen)
2. Wurde von einer Beteiligten verfasst oder empfangen und datiert auf den
 relevanten Tatzeitraum
3. Enthält Schlüsselwörter zum Vorwurfstyp (aus der Sachverhaltserfassung
 und aus früheren Protokolleinträgen — Stichwortliste laufend ergänzen)
4. Enthält explizite oder implizite Selbstbelastungen (z. B. "das hätte ich
 nicht tun sollen", "ich weiß, wie das aussieht", "schreib das nicht auf",
 "lösch das")
5. Enthält Aussagen, die einem bereits protokollierten Zeugenbericht
 widersprechen — Widerspruch und den betroffenen Protokolleintrag benennen
6. Enthält sprach- oder inhaltlich sensibles Material: diskriminierende
 Ausdrücke, Drohungen, Bezugnahmen auf geschützte Merkmale (§ 1 AGG),
 Unregelmäßigkeiten, die dem Vorwurfsmuster entsprechen
7. Ist ein Dokumententyp, der in früheren Schilderungen erwähnt, aber noch
 nicht im Dokumentensatz aufgetaucht ist → als Beweislücke protokollieren,
 nicht als Treffer

**Disposition für jedes geprüfte Dokument:**
- `relevant`: erfüllt eines oder mehrere Auswahlkriterien — als Protokolleintrag hinzufügen
- `geprueft-nicht-relevant`: geprüft, kein Auswahlkriterium erfüllt —
 in dokumente-geprueft.yaml mit einem Satz beschreiben

**Nach Bearbeitung eines Dokumentenpakets melden:**

```
Dokumentenprüfung abgeschlossen.
Geprüft: [N] Dokumente
Relevant: [N]
Geprüft / nicht relevant: [N]
Neue Beweislücken: [N]

Relevante Dokumente:
[Liste mit einem Satz Beschreibung und dem Auswahlkriterium, das angesprungen ist]
```

### Schritt 4 — Protokolleinträge schreiben

Für jeden relevanten Fund, Anhang an log.yaml:

```yaml
- eintrag_id: [fortlaufend]
 eintrag_typ: [befragung / dokument / anwaltsnotiz / beweislücke]
 ereignis_datum: "[Datum des Ereignisses — nicht das Protokolldatum]"
 protokoll_datum: "[ISO-Datetime]"
 quelle: "[Name/Funktion der befragten Person oder Dokumentenbeschreibung]"
 quellen_typ: [beschwerdefuehrer / beschuldigter / zeuge / dokument / anwaltsnotiz]
 fragen: ["[welcher Untersuchungsfrage/-n ist dieser Eintrag zuzuordnen]"]
 bedeutung: [hoch / mittel / hintergrund]
 zusammenfassung: "[was dieser Eintrag zum Erkenntnisstand beiträgt — 2–5 Sätze]"
 zitat: "[wörtliches Zitat wenn bedeutsam — sonst leer]"
 widerspricht_eintrag: [eintrag_id oder null]
 bestaetigt_eintrag: [eintrag_id oder null]
 glaubwuerdigkeitsnotiz: ""
 auswahlkriterium: "[welches Kriterium hat angesprochen — für Dokumente]"
 vertraulich: arbeitsrechtlich-intern
```

Für Beweislücken:

```yaml
- luecke_id: [fortlaufend]
 beschreibung: "[welches Dokument/welche Quelle sollte existieren, fehlt aber]"
 identifiziert_aus: "[welcher Protokolleintrag oder Bericht hat darauf hingewiesen]"
 beschaffungsweg: "[wo es zu bekommen wäre]"
 prioritaet: [hoch / mittel / gering]
 status: offen
```

---

## Modus 3: Protokoll abfragen

Ausgelöst durch `/arbeitsrecht:untersuchung-abfrage`.

Gesamtes Protokoll lesen vor der Antwort. Antworttypen:

**Sachverhaltsabfrage** ("Was hat [Person] zu [Thema] gesagt?"):
Aus den Protokolleinträgen antworten, Eintrags-IDs zitieren. Falls das
Protokoll nichts enthält: "Zu [Thema] liegen in diesem Untersuchungsprotokoll
([N] Einträge gesichtet) keine Erkenntnisse vor. Dies sollte ggf. als
Beweislücke erfasst werden."

**Widerspruchsabfrage** ("Wo widersprechen sich die Schilderungen?"):
Alle widerspricht_eintrag-Verknüpfungen zeigen. Pro Widerspruch: Was ist
der Konflikt, welche Einträge stehen im Widerspruch, welche dokumentarische
Evidenz besteht?

**Deckungsabfrage** ("Was fehlt noch?" / "Wo haben wir Lücken?"):
quellen-checkliste.yaml und beweislücken im log.yaml auslesen. Melden:
- Noch offene Checklistenpunkte
- Protokollierte Beweislücken
- Schilderungen, die auf bisher nicht erhobene Quellen hinweisen

**Stärkeabfrage** ("Was ist die stärkste Evidenz zu jeder Frage?"):
Für jede Untersuchungsfrage: höchstbewertete Protokolleinträge, dokumentarische
Bestätigungen und ungelöste Widersprüche — frageweise strukturiert.

---

## Modus 4: Memo entwerfen oder aktualisieren

Ausgelöst durch `/arbeitsrecht:untersuchungs-memo`.

### Erstmalige Erstellung

Gesamtes Protokoll lesen. Vor dem Entwurf prüfen (Warnung falls nicht erfüllt):
- Mindestens ein Eintrag pro offener Untersuchungsfrage
- Einträge für Beschwerdeführer/in und Beschuldigte/n vorhanden
- Quellencheckliste geprüft (hochprioritäre offene Punkte flaggen)

Memo in folgender Struktur:

```markdown
VERTRAULICH — INTERNE UNTERSUCHUNG — [Datum]

---

**VERMERK**

An: [Anwalt eintragen]
Von: [Anwalt eintragen]
Datum: [Datum]
Betr.: Interne Untersuchung — [Sachbezeichnung]
Stand: VORENTWURF

---

## Zusammenfassung

[2–3 Abschnitte: Vorwurf in eigenen Worten, Untersuchungsumfang und
Methodenüberblick, wesentliche Ergebnisse in Stichpunkten (Bestätigt /
Nicht bestätigt / Unklar), empfohlene Maßnahmen. Wird zuletzt geschrieben,
erscheint zuerst.]

---

## Hintergrund und Untersuchungsumfang

**Auslöser:** [Was hat die Untersuchung ausgelöst]

**Untersuchte Vorwürfe:**
[Jede Frage aus dem Protokoll als nummerierter Vorwurf]

**Nicht Untersuchtes:** [Was ausdrücklich ausgeklammert wurde und warum]

**Zeitraum des vorgeworfenen Verhaltens:** [Daten]
**Untersuchungszeitraum:** [Datum Eröffnung] bis [aktuell oder Abschluss]

---

## Methodik

**Durchgeführte Anhörungen:**
| Person | Funktion | Datum | Hinweise |
|---|---|---|---|

**Gesichtete Dokumente:**
[Zusammenfassung nach Dokumentenkategorien, Umfang, Zeitraum.
Vollständiges Dokumentenprotokoll separat geführt.]

**Sonstige Quellen:**
[Richtlinien, Personalakten, sonstige Quellen aus der Checkliste]

**Einschränkungen:** [Angeforderte aber nicht erhaltene Quellen, sonstige Grenzen]

---

## Sachverhaltliche Feststellungen

*[Nach Fragen gegliedert — ein Abschnitt pro Vorwurf. Nicht nach Zeuge,
nicht rein chronologisch.]*

### Frage 1: [Vorwurf]

[Narrative Darstellung der Erkenntnislage. Eintrags-IDs in Klammern zitieren.
Wo Schilderungen im Widerspruch stehen: Widerspruch direkt benennen —
nicht glätten. Dokumentarische Belege mit Zitaten wenn bedeutsam.]

---

## Glaubwürdigkeitsbewertung

*[Eigenständiger Abschnitt. Nur Personen, deren Glaubwürdigkeit entscheidungserheblich
ist — d. h. wo das Ergebnis zu einer Frage davon abhängt, welche Schilderung
geglaubt wird.]*

### [Name/Funktion]

**Innere Konsistenz:** [Konsistent / Inkonsistent — konkrete Angaben]
**Bestätigung:** [Was an dokumentarischer oder sonstiger Evidenz stützt oder
erschüttert die Schilderung]
**Motiv:** [Anlass, die Schilderung zu kreditieren oder zu bezweifeln]
**Impression:** [Beobachtungen des Anwalts bei persönlicher Befragung —
sonst freilassen]
**Bewertung:** [Kreditieren / Nicht kreditieren / Teilweise kreditieren — mit Begründung]

---

## Einschlägige Regelungen

[Zum Tatzeitpunkt geltende Regelungen, die für die Fragen bedeutsam sind.
Version angeben. Keine nach dem Vorfall eingeführten Regelungen zitieren.]

---

## Ergebnisse

| Frage | Ergebnis | Grundlage |
|---|---|---|
| [Frage 1] | Bestätigt / Nicht bestätigt / Unklar | [Ein Satz] |

*Ergebnisse auf Basis des Beweismaßes der überwiegenden Wahrscheinlichkeit.*

---

## Empfehlungen

**Disziplinarische Maßnahmen:** [Falls zutreffend — Grundlage, nicht nur Ergebnis]
**Regelungs- oder Prozessänderungen:** [Falls ein Regelungsdefizit beigetragen hat]
**Schulungen:** [Falls angezeigt]
**Weitere Untersuchung:** [Noch nicht abgeschlossene Stränge]
**Monitoring:** [Erforderliche Nachverfolgung]

---

## Anlage A: Chronologie

[Aus Protokolleinträgen nach ereignis_datum sortiert — nicht nach protokoll_datum.
Format: Datum | Zusammenfassung | Quelle (Eintrags-ID)]

## Anlage B: Gesichtete Dokumente

[Übersichtstabelle aus dokumente-geprueft.yaml]
```

### Falls Memo bereits existiert — Aktualisierung

Memo und Protokoll lesen. Seit dem letzten Entwurf hinzugekommene Einträge
identifizieren.

Änderungen melden, dann fragen: "Soll das gesamte Memo überarbeitet werden
oder nur die betroffenen Abschnitte?"

Änderungen einarbeiten. Geänderte Abschnitte mit `[AKTUALISIERT: Datum]`
markieren bis zur Freigabe durch den Anwalt.

---

## Modus 5: Zielgruppen-Zusammenfassung

Ausgelöst durch `/arbeitsrecht:untersuchungs-zusammenfassung`.

Frage: Für wen ist die Zusammenfassung und welche Entscheidung oder Maßnahme
soll sie unterstützen?

**HR-Zusammenfassung** (für disziplinarische Entscheidung):
- Was ist passiert (Sachverhaltsdarstellung, keine Rechtsanalyse)
- Ergebnis zu jedem Vorwurf (Bestätigt / Nicht bestätigt / Unklar)
- Empfohlene Maßnahme
- Nicht enthalten: Glaubwürdigkeitsmethodik, Rechtsrisikoanalyse,
 anwaltliche Eindrücke
- Kopfzeile: "Vertraulich — Nur für HR — Keine Weitergabe"
- Keine Eintrags-IDs oder Dokumentenverweise

**Geschäftsführung / Aufsichtsrat** (für Governance-Entscheidung):
- Vorwurf und Umfang in einem Abschnitt
- Wesentliche Ergebnisse
- Unternehmensrelevanz / Expositionseinschätzung (nur grob — keine Detailrechtsanalyse)
- Ergriffene und geplante Maßnahmen
- Kopfzeile: "Vertraulich — Interne Untersuchung"

**Externe Bevollmächtigte** (für Prozessvorbereitung oder vertiefende Prüfung):
- Vollständiger Kontext einschließlich Rechtsrisikoanalyse
- Offene Beweisstränge
- Ungelöste Glaubwürdigkeitsfragen
- Dokumente mit erhöhter Prozeßrelevanz

---

## Was diese Skill nicht tut

- Disziplinarische Entscheidungen treffen — sie unterstützt die anwaltlichen
 Feststellungen, nicht die HR-Entscheidung
- Vertraulichkeitsschutz garantieren — Schutz hängt davon ab, wie die
 Untersuchung strukturiert und wie Materialien verteilt wurden
- Dokumente lesen, die technisch nicht verarbeitbar sind — solche Dateien
 für manuelle Prüfung flaggen
- Befragungen durchführen — Befragungsnotizen werden protokolliert,
 nicht selbst geführt
- Anhörungshinweise ersetzen — sie verfolgt, ob sie erteilt wurden,
 erteilt sie nicht selbst

## Quellenpflicht

Bei jeder Ausgabe zu Untersuchungsverfahren zitieren:
- § 26 BDSG (Beschäftigtendatenschutz, Verhältnismäßigkeit)
- § 87 Abs. 1 Nr. 6 BetrVG (Mitbestimmung bei technischer Überwachung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Beschäftigtendatenschutz: § 26 BDSG, Art. 5 und 6 DSGVO; Fachliteratur nur mit Nutzerquelle oder verifiziertem Live-Zugriff.
- § 626 BGB: Zwei-Wochen-Frist, Verdachtskündigung und Anhörung nur mit verifizierter BAG-Rechtsprechung oder Nutzerquelle vertiefen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 3. `kuendigungs-pruefung`

**Fokus:** Rechtliche Prüfung einer ordentlichen oder außerordentlichen Kündigung – KSchG (allgemeiner und besonderer Kündigungsschutz), § 102 BetrVG (Betriebsratsanhörung), §§ 622 und 626 BGB (Fristen und wichtiger Grund), Sozialauswahl § 1 Abs. 3 KSchG, Sonderkündigungsschutz (MuSchG, BEEG, SGB IX, § 15 KSchG).

### /arbeitsrecht:kündigungs-prüfung

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:kündigungs-prüfung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Die meisten Kündigungen sind rechtlich unproblematisch. Einige sind Klagen, die noch nicht eingereicht wurden. Dieser Skill findet die Hochrisikofälle, bevor die 3-Wochen-Frist des § 4 KSchG beginnt zu laufen: Sonderkündigungsschutz, fehlende Betriebsratsanhörung, mangelhafte Sozialauswahl, unzureichende Dokumentation.

## Eingaben

- Kündigungsanlass (betriebsbedingt / verhaltensbedingt / personenbedingt)
- Angaben zum Arbeitnehmer: Beschäftigungsdauer, Position, Gehaltsgruppe, Familienstand (für Sozialauswahl), Schwerbehinderung, Betriebsratsmandat, Schwangerschaft/Elternzeit
- Angaben zum Betrieb: Mitarbeiterzahl (KSchG § 23), Betriebsrat vorhanden?
- Vorherige Abmahnungen? (für verhaltensbedingte Kündigung)
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Kündigungsregeln, Eskalation

## Ablauf

### 1. Vorprüfung: Anwendungsbereich KSchG (§ 23 KSchG)

**Schwellenwert:** KSchG gilt für Arbeitnehmer, die länger als 6 Monate beschäftigt sind (§ 1 Abs. 1 KSchG), wenn im Betrieb **mehr als 10 Arbeitnehmer** i.S.d. § 23 KSchG beschäftigt sind (Vollzeitkräfte zählen voll; Teilzeitkräfte bis 20 h = 0,5; bis 30 h = 0,75; Leiharbeitnehmer ohne Berücksichtigung).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 2. Sonderkündigungsschutz-Check (vor allem anderen)

Bei Vorliegen eines der folgenden Merkmale: **🔴 Blockierend – sofortige Eskalation**

| Schutztatbestand | Norm | Anforderung |
|---|---|---|
| Schwangerschaft / Mutterschutz | § 17 MuSchG | Zustimmung zuständige Behörde (Amt für Arbeitsschutz) vor Ausspruch |
| Elternzeit | § 18 BEEG | Zustimmung zuständige Behörde; Ausnahme bei schwerwiegenden Gründen § 18 Abs. 1 S. 2 BEEG |
| Schwerbehinderte / Gleichgestellte | § 168 SGB IX | Zustimmung Inklusionsamt (früher: Integrationsamt) vor Ausspruch; 3-Wochen-Antragsfrist |
| Betriebsratsmitglied, Wahlvorstand u.a. | § 15 KSchG | Ordentliche Kündigung ausgeschlossen; ao. Kündigung § 103 BetrVG (BR-Zustimmung) |
| Datenschutzbeauftragter | § 38 Abs. 2 BDSG i.V.m. § 6 Abs. 4 BDSG | Kündigungsschutz während Amtszeit + 1 Jahr danach |
| Elternzeitbeantragung | § 18 Abs. 1 BEEG | Beginnt ab Antragstellung |
| Pflegezeit | § 5 PflegeZG | Schutz wie BEEG |

### 3. Betriebsratsanhörung (§ 102 BetrVG)

Falls Betriebsrat vorhanden: **Jede Kündigung vor Ausspruch anhören.** Ohne ordnungsgemäße Anhörung ist die Kündigung unwirksam (§ 102 Abs. 1 S. 3 BetrVG).

Checkliste:
- Ist der BR schriftlich informiert worden?
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Frist abgewartet? (ordentlich: 1 Woche; außerordentlich: 3 Tage; § 102 Abs. 2 BetrVG)
- Ordnungsgemäße Bedenken des BR beachtet (keine Vetorechte bei ordentlicher Kündigung, aber Widerspruch nach § 102 Abs. 3 BetrVG gibt Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG)

Verweis auf separaten Skill: `/arbeitsrecht:betriebsrat-anhörung`

### 4. Prüfung des Kündigungsgrunds (§ 1 KSchG)

**A – Betriebsbedingte Kündigung:**

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. **Wegfall des Arbeitsplatzes:** Konkret und dauerhaft; bloße Umsatzrückgänge genügen nicht
3. **Weiterbeschäftigung auf freiem vergleichbaren Arbeitsplatz** ausgeschlossen (§ 1 Abs. 2 S. 2 KSchG)
4. **Sozialauswahl (§ 1 Abs. 3 KSchG)** – zentraler Prüfpunkt (siehe unten)
5. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Sozialauswahl (§ 1 Abs. 3 KSchG):**

Unter vergleichbaren Arbeitnehmern müssen die sozial am wenigsten schutzwürdigen entlassen werden. Kriterien:
- Betriebszugehörigkeit
- Lebensalter
- Unterhaltsverpflichtungen
- Schwerbehinderung

Prüfschema:
1. Vergleichsgruppe bilden (gleiche Hierarchieebene, austauschbar durch Einarbeitung ≤ 3 Monate)
2. Sozialpunkte berechnen (§ 1 Abs. 3 S. 1 KSchG; keine gesetzliche Punktetabelle – Betriebsvereinbarung oder Interessenausgleich empfohlen)
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**B – Verhaltensbedingte Kündigung:**

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. **Interessenabwägung:** Schwere der Pflichtverletzung vs. Dauer der Beschäftigung, Sozialauswahl, Wiederholungsgefahr

Verweis auf separaten Skill: `/arbeitsrecht:abmahnung-arbeitsrecht`

**C – Personenbedingte Kündigung (insb. krankheitsbedingt):**

1. **Prognose negativer Art:** Weitere erhebliche Fehlzeiten zu erwarten?
2. **Betriebliche Beeinträchtigung:** Erhebliche Störung des Betriebsablaufs oder Entgeltfortzahlungskosten > 6 Wochen p.a.?
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 5. Kündigungsfristen (§ 622 BGB / Tarifvertrag)

| Beschäftigungsdauer | Frist (§ 622 Abs. 2 BGB) |
|---|---|
| 0–2 Jahre | 4 Wochen zum 15. oder Monatsende |
| 2–5 Jahre | 1 Monat zum Monatsende |
| 5–8 Jahre | 2 Monate |
| 8–10 Jahre | 3 Monate |
| 10–12 Jahre | 4 Monate |
| 12–15 Jahre | 5 Monate |
| 15–20 Jahre | 6 Monate |
| > 20 Jahre | 7 Monate |

Tarifvertragliche Abweichungen prüfen! Ggf. günstigere Individualvereinbarung.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 6. Abfindungsangebot (§ 1a KSchG)

Arbeitgeber kann mit der Kündigung eine Abfindung nach § 1a KSchG anbieten (0,5 Monatsgehalt × Beschäftigungsjahre), wenn Arbeitnehmer keine Klage erhebt. Dies schließt Wiedereinstellungsansprüche aus.

### 7. DSGVO-Auskunftsersuchen als Druckmittel im Kündigungskontext

**Typische Konstellation:** Unmittelbar vor oder nach Ausspruch der Kündigung – oft zeitgleich mit der Ankündigung einer KSchG-Klage – stellt der Arbeitnehmer oder sein Bevollmächtigter ein Auskunftsersuchen nach Art. 15 DSGVO. Ziel ist häufig, über den Umweg des Datenschutzrechts Einblick in interne Personalakten, Abmahnungsunterlagen oder Vermerke zu erlangen und so den Arbeitgeber unter Vergleichsdruck zu setzen.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Ein Auskunftsersuchen kann nach Art. 12 Abs. 5 S. 2 DSGVO als exzessiv abgelehnt oder mit angemessenen Kosten belegt werden, wenn der Verantwortliche (Arbeitgeber) zwei Elemente nachweist:

1. **Objektives Element:** Äußere Umstände lassen auf missbräuchliche Zweckverfolgung schließen — z. B. ungewöhnlich kurzer zeitlicher Abstand zwischen Zugang der Kündigung und Auskunftsantrag, Muster massenhafter Legal-Tech-gestützter Antragstellung, Anmeldung zur Datenverarbeitung allein zum Zweck der Anfrage.
2. **Subjektives Element:** Missbräuchliche Absicht — Instrumentalisierung des Auskunftsrechts vorrangig zur Generierung von Schadensersatzansprüchen nach Art. 82 DSGVO oder zur Prozesstaktik, nicht zum Schutz personenbezogener Daten.

Hürden sind **hoch**: Das Auskunftsrecht ist ein Grundrecht (Art. 8 GRCh); Ausnahmen sind eng auszulegen. Auch ein erstmaliges Ersuchen kann exzessiv sein, aber bloße Mehrfachanträge oder die bloße Tatsache vergangener Auskunftsansprüche genügen nicht.

**BAG-Linie zu Art. 82 DSGVO:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Praxishinweise für den Arbeitgeber:**
- DSGVO-Auskunft fristgerecht innerhalb eines Monats beantworten (Art. 12 Abs. 3 DSGVO); unberechtigte Ablehnung kann eigenständigen Schadensersatzanspruch nach Art. 82 DSGVO auslösen.
- Dokumentation für Missbrauchseinwand anlegen: Datum Kündigung, Datum Auskunftsantrag, Vorliegen von Legal-Tech-Vollmacht, Muster bei anderen Mitarbeitern.
- Parallellauf Kündigungsschutzverfahren und DSGVO-Auskunftsstreit im Blick behalten: Zuständiges Gericht für Auskunftsklage ist nach Art. 79 DSGVO i.V.m. § 44 BDSG das Landgericht (nicht das Arbeitsgericht); Koordinierung der Prozesstaktik erforderlich.

Querverweis: `datenschutzrecht/skills/dsgvo-auskunft/SKILL.md` (soweit im Plugin vorhanden).

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Wesentliche Quellen:
- Dörner/Vossen, in: KR, 13. Aufl. 2022, § 1 KSchG Rn. 1 ff. (Sozialauswahl)
- Becker/Wolff, in: APS, 6. Aufl. 2021, § 1 KSchG Rn. 500 ff. (betriebsbedingte Kündigung)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

Strukturierte Kündigungsprüfung als Memo:

```
KÜNDIGUNGSPRÜFUNG – [Arbeitnehmer-ID/Position] – [Datum]
VERTRAULICH – MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

Ergebnis: [🟢 Kündigung rechtlich möglich / 🟡 Kündigung möglich mit Auflagen / 🔴 Kündigung nicht empfohlen]

⚠️ Prüfhinweis: [Quellen, Flags, Aktualität]

I. KSchG-Anwendungsbereich [🟢 / 🟡 / N/A]
II. Sonderkündigungsschutz-Check [🟢 / 🔴 Flag: ...]
III. Betriebsratsanhörung [🟢 / 🔴 ausstehend]
IV. Kündigungsgrund (§ 1 KSchG) [🟢 / 🟡 / 🔴]
 Typ: [betriebsbedingt / verhaltensbedingt / personenbedingt]
 Begründung: ...
V. Sozialauswahl (falls bb.) [🟢 / 🟡 / 🔴]
 Vergleichsgruppe: [N AN]
 Sozialpunkte: [Tabelle]
VI. Kündigungsfrist [Frist]
VII. Abfindungsangebot (optional) [§ 1a KSchG Betrag]

Offene Flaggen: [Liste mit [prüfen]-Markierungen]
Eskalation: [ja/nein – Begründung]

Wie weiter? [Entscheidungsbaum]
```

## Beispiele

**Beispiel – Betriebsbedingte Kündigung mit Sozialauswahl:**

*Sachverhalt:* Mandant (Maschinenbauunternehmen, 35 AN, kein BR) will eine von drei Stellen im Bereich Vertriebsinnendienst streichen. Drei Arbeitnehmer: A (10 Jahre, 45 Jahre, 2 Kinder), B (3 Jahre, 30 Jahre, ledig, anerkannte Schwerbehinderte GdB 50), C (8 Jahre, 55 Jahre, geschieden, 1 Kind).

*Ergebnis (Urteilsstil):*

Die beabsichtigte Kündigung ist der des Arbeitnehmers C am ehesten begründbar. In der Sozialauswahl nach § 1 Abs. 3 KSchG sind alle drei Arbeitnehmer in eine Vergleichsgruppe einzustellen (gleiche Funktion, Austauschbarkeit gegeben). Arbeitnehmer B genießt Sonderkündigungsschutz nach § 168 SGB IX; eine Kündigung erfordert Zustimmung des Inklusionsamts (🔴 Blockierend). A und C stehen im direkten Auswahlvergleich: Die längere Betriebszugehörigkeit von A (10 Jahre), sein Lebensalter (45 J.) und die Unterhaltsverpflichtungen (2 Kinder) überwiegen die Schutzwürdigkeit von C (8 Jahre, 55 Jahre, 1 Kind). C ist nach Sozialpunkten am wenigsten schutzwürdig – Kündigung sozialauswahl-konform, wenn Interessenausgleich dokumentiert wird.

🟠 Empfehlung: Vor Ausspruch formlose (da kein BR vorhanden) Kündigung und schriftliche Sozialauswahldokumentation erstellen. Abfindungsangebot gem. § 1a KSchG erwägen.

## Risiken / typische Fehler

- **Massenentlassungsanzeige vergessen** (§§ 17–18 KSchG) – führt zur Unwirksamkeit aller Kündigungen; Schwellenwerte im Blick behalten.
- **Betriebsratsanhörung inhaltlich unvollständig** – fehlende Angaben zur Person oder zum Kündigungsgrund machen Anhörung unwirksam (§ 102 Abs. 1 S. 3 BetrVG).
- **Sonderkündigungsschutz übersehen** – insbesondere bei Betriebsratsmitgliedern, Schwangeren, Elternzeitnehmenden.
- **Sozialauswahl ohne Dokumentation** – bei Klagefrist-Ablauf (§ 4 KSchG) kaum nachrüstbar; immer schriftlich begründen.
- **2-Wochen-Frist § 626 Abs. 2 BGB** – beginnt mit positiver Kenntnis des Kündigungsberechtigten, nicht mit vager Vermutung.
- **BEM nicht durchgeführt** – erhöhte Darlegungslast; vor krankheitsbedingter Kündigung dokumentieren.

## 4. `kuendigungsschutzklage`

**Fokus:** Prüft und entwirft eine Kündigungsschutzklage nach § 4 KSchG. Lädt, wenn ein Arbeitnehmer eine ordentliche oder außerordentliche Kündigung anfechten will, die 3-Wochen-Frist droht oder ein Entwurf des Klageantrags, der Klagebegründung und der Sozialauswahl benötigt wird.

### Kündigungsschutzklage (§ 4 KSchG)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kündigungsschutzklage (§ 4 KSchG)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill unterstützt bei der Prüfung und dem Entwurf einer Kündigungsschutzklage nach § 4 KSchG. Er dient Rechtsanwältinnen und Rechtsanwälten, die ein Mandat zur Überprüfung einer Arbeitgeberkündigung führen, sowie der internen Fallanalyse. Kernproblem ist regelmäßig die **3-Wochen-Klagefrist** (§ 4 Satz 1 KSchG), die ab Zugang der Kündigung läuft und bei Versäumung zum Verlust des Kündigungsschutzrechts führt (§ 7 KSchG). Der Skill erfasst sowohl ordentliche als auch außerordentliche Kündigungen, die Sozialauswahl, die Betriebsratsanhörung und die gerichtliche Geltendmachung.

## Eingaben

Für eine vollständige Bearbeitung werden benötigt:

1. **Kündigungsschreiben** (Text oder Scan) – Datum der Ausfertigung und des Zugangs
2. **Arbeitsverhältnis**: Beginn, Beendigungsdatum laut Kündigung, Vollzeit/Teilzeit
3. **Betriebsgröße**: Anzahl der wahlberechtigten Arbeitnehmer (§ 1 Abs. 1 KSchG: regelmäßig mehr als 10)
4. **Kündigungstyp**: ordentlich (§ 1 KSchG) oder außerordentlich (§ 626 BGB)
5. **Kündigungsgrund**: betriebsbedingt, personenbedingt oder verhaltensbedingt
6. **Betriebsrat vorhanden?** Falls ja: Anhörungsunterlagen (§ 102 BetrVG)
7. **Sozialauswahl** (bei betriebsbedingter Kündigung): vergleichbare Arbeitnehmer, Sozialdaten (Alter, Betriebszugehörigkeit, Unterhaltspflichten, Schwerbehinderung)
8. **Bisherige Abmahnungen** (Datum, Inhalt)
9. **Sonderkündigungsschutz**: Schwangerschaft, Elternzeit, Schwerbehinderung, BR-/JAV-Mitgliedschaft

## Rechtlicher Rahmen

### Kernvorschriften

- § 4 Satz 1 KSchG: Klagefrist 3 Wochen ab Zugang der Kündigung (absolute Ausschlussfrist, keine Hemmung)
- § 7 KSchG: Fiktionswirkung – Kündigung gilt als rechtswirksam, wenn nicht rechtzeitig Klage erhoben
- § 1 Abs. 1 KSchG: Geltungsbereich (6 Monate Wartezeit, Betrieb > 10 AN)
- § 1 Abs. 2 KSchG: Soziale Rechtfertigung (betriebs-, personen-, verhaltensbedingt)
- § 1 Abs. 3 KSchG: Sozialauswahl bei betriebsbedingter Kündigung
- § 626 Abs. 1 BGB: Außerordentliche Kündigung aus wichtigem Grund
- § 626 Abs. 2 BGB: 2-Wochen-Frist für außerordentliche Kündigung
- § 102 BetrVG: Anhörung des Betriebsrats vor jeder Kündigung
- §§ 46 ff. ArbGG: Zuständigkeit und Verfahren Arbeitsgericht
- § 256 ZPO: Feststellungsklage (entsprechend anwendbar über § 46 Abs. 2 ArbGG)

### Leitentscheidungen (BGH-Stil, Stand Mai 2026)

- **Massenentlassung - Fehler im Anzeigeverfahren:**
 BAG, Urteile vom 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22: Fehlende oder verfruehte (vor Abschluss der BR-Konsultation eingereichte) Massenentlassungsanzeige fuehrt zur Unwirksamkeit aller davon erfassten Kuendigungen; keine Heilung nach Kuendigungsausspruch. Quelle: dejure.org-Vernetzung; BAG-Pressemitteilung "Massenentlassung - Rechtsfolge von Fehlern im Anzeigeverfahren". Zugehoeriger EuGH: 30.10.2025 - C-134/24 und C-402/24.

- **Freistellungsklausel im Arbeitsvertrag:**
 BAG, Urteil vom 25.03.2026 - 5 AZR 108/25: Pauschale formularmäßige Freistellungsklausel benachteiligt den Arbeitnehmer unangemessen (§ 307 Abs. 1 Satz 1 BGB); der Beschaeftigungsanspruch ueberwiegt das pauschale Freistellungsinteresse. Quelle: dejure.org-Vernetzung.

- **Mindesturlaubsverzicht im Prozessvergleich:**
 BAG, Urteil vom 03.06.2025 - 9 AZR 104/24: Pauschale Erledigungsklausel erfasst den gesetzlichen Mindesturlaub im laufenden Arbeitsverhaeltnis nicht wirksam; § 13 Abs. 1 Satz 3 BUrlG i.V.m. RL 2003/88/EG. Quelle: dejure.org-Vernetzung.

- **Equal Pay / Paarvergleich:**
 BAG, Urteil vom 23.10.2025 - 8 AZR 300/24: Paarvergleich mit einem einzelnen Vergleichskollegen des anderen Geschlechts genuegt für die Vermutung nach § 22 AGG; Mediane oder Vergleichsgruppengroessen sind irrelevant. Quelle: dejure.org-Vernetzung.

- **DSGVO-Schadensersatz bei verspaeteter Auskunft:**
 BAG, Urteil vom 20.02.2025 - 8 AZR 61/24: "Stoergefuehl" allein begruendet keinen Schadensersatzanspruch nach Art. 82 DSGVO; konkrete Kontrollverlust-Furcht oder tatsaechlicher Schaden erforderlich. Quelle: dejure.org-Vernetzung; Volltext-PDF auf bundesarbeitsgericht.de.

- **Arbeitszeiterfassung:**
 BAG, Beschluss vom 13.09.2022 - 1 ABR 22/21: Pflicht des Arbeitgebers zur Erfassung der gesamten Arbeitszeit aus § 3 Abs. 2 Nr. 1 ArbSchG. Quelle: dejure.org-Vernetzung.

- **NachweisG-Schadensersatz:**
 BAG, Urteil vom 22.09.2022 - 8 AZR 4/21: Bei Verstoss gegen NachwG kann der Arbeitnehmer Schadensersatz verlangen, soweit die Pflichtverletzung kausal für den Schaden war; Anspruch nicht auf Bussgeldhoehe begrenzt. Quelle: dejure.org-Vernetzung.

- **Subjektive Determinationstheorie BR-Anhörung:**
 BAG, 27.02.1997 - 2 AZR 302/96 (Standardlinie); BAG, 05.02.1998 - 2 AZR 227/97. Quelle: dejure.org-Vernetzung.

Allgemein: Weitere Entscheidungen zu Sozialauswahl, betriebsbedingter Kuendigung, wichtigem Grund usw. vor Schriftsatzverwendung in offenen Quellen (dejure.org / openjur.de / bundesarbeitsgericht.de) verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Schritt 1 – Fristprüfung (KRITISCH, SOFORT)

1. Zugangsdatum der Kündigung feststellen (Zeugen, Einschreiben-Rückschein, Übergabe-Quittung).
2. Klagefrist berechnen: 3 Wochen ab Zugang, §§ 4, 7 KSchG; keine Hemmung möglich.
3. Falls Frist abgelaufen: Nachzulassungsantrag nach § 5 KSchG prüfen (unverschuldete Versäumung, z. B. Krankheit, Abwesenheit); Frist: 2 Wochen nach Wegfall des Hindernisses.
4. Mandanten sofort über Fristablauf und Konsequenzen (§ 7 KSchG) belehren; Belehrung dokumentieren.

### Schritt 2 – Geltungsbereich KSchG

- Wartezeit ≥ 6 Monate (§ 1 Abs. 1 KSchG)?
- Betriebsgröße: mehr als 10 Arbeitnehmer i. S. v. § 23 Abs. 1 KSchG (Teilzeit anteilig)?
- Falls KSchG nicht anwendbar: allgemeiner Kündigungsschutz (§§ 138, 242 BGB), Sonderkündigungsschutz (MuSchG, BEEG, SGB IX, § 15 KSchG) gesondert prüfen.

### Schritt 3 – Prüfung der sozialen Rechtfertigung (§ 1 KSchG)

**A. Betriebsbedingte Kündigung**
- Unternehmerische Entscheidung? Dauerhafter Wegfall des Beschäftigungsbedarfs?
- Weiterbeschäftigungsmöglichkeit (freier Arbeitsplatz, ggf. nach Änderungskündigung)?
- Sozialauswahl § 1 Abs. 3 KSchG: Kreis der vergleichbaren Arbeitnehmer bestimmen, Sozialpunkte (Alter, Betriebszugehörigkeit, Unterhaltspflichten, Schwerbehinderung) ermitteln, Ausnahmen (Leistungsträger § 1 Abs. 3 Satz 2 KSchG).

**B. Personenbedingte Kündigung**
- Negative Prognose (dauerhafter Leistungsausfall), Erheblichkeit, Interessenabwägung.
- Häufig: Krankheit (BAG-Dreistufenprüfung: Negativprognose, erhebliche Beeinträchtigung, Interessenabwägung).

**C. Verhaltensbedingte Kündigung**
- Pflichtverletzung (schuldhaft), Abmahnung als Voraussetzung (Warn- und Rügefunktion), negative Prognose, Verhältnismäßigkeit.

### Schritt 4 – Betriebsratsanhörung (§ 102 BetrVG)

- BR vor Ausspruch der Kündigung angehört?
- Inhalt der Mitteilung vollständig (Sozialdaten, Kündigungsgrund, Art der Kündigung)?
- Frist eingehalten (1 Woche ordentlich, 3 Tage außerordentlich)?
- Widerspruch des BR nach § 102 Abs. 3 BetrVG → Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG.
- Fehler der BR-Anhörung → Kündigung unwirksam (§ 102 Abs. 1 Satz 3 BetrVG).

### Schritt 5 – Außerordentliche Kündigung (§ 626 BGB)

- Wichtiger Grund i. S. v. § 626 Abs. 1 BGB: Unzumutbarkeit der Fortsetzung bis Ablauf der ordentlichen Frist?
- 2-Wochen-Frist § 626 Abs. 2 BGB: ab Kenntnis des Kündigungsberechtigten; Fristversäumung → Kündigung unwirksam.
- Interessenabwägung: alle Umstände des Einzelfalls (Betriebszugehörigkeit, Vorleben, Art und Schwere der Pflichtverletzung).

### Schritt 6 – Klageschrift verfassen

**Rubrum:** Arbeitsgericht [Ort] (§ 46 Abs. 2 ArbGG i. V. m. § 253 ZPO), Kläger = Arbeitnehmer, Beklagte = Arbeitgeberin.

**Klageanträge (Feststellungsklage):**
```
1. Es wird festgestellt, dass das Arbeitsverhältnis der Parteien durch die Kündigung
 der Beklagten vom [Datum], zugegangen am [Datum], nicht aufgelöst worden ist.

2. [Hilfsweise: Es wird festgestellt, dass das Arbeitsverhältnis auch nicht durch
 andere Beendigungsgründe endet, sondern über den [Datum] hinaus fortbesteht.]

3. [Weiterbeschäftigungsantrag nach § 102 Abs. 5 BetrVG / allg. Weiterbeschäftigung
 bis Rechtskraft des Urteils, soweit Widerspruch des BR oder schutzwürdiges Interesse.]
```

**Begründung (Struktur):**
1. Sachverhalt / Arbeitsverhältnis
2. KSchG-Geltungsbereich (Wartezeit, Betriebsgröße)
3. Fehlende soziale Rechtfertigung (je nach Kündigungsart, s. Schritt 3)
4. Fehler der BR-Anhörung (sofern einschlägig)
5. Sonderkündigungsschutz (sofern einschlägig)
6. Beweisangebote

### Schritt 7 – Einreichung und Gütetermin

- Klage beim örtlich zuständigen Arbeitsgericht (§ 48 ArbGG i. V. m. §§ 12 ff. ZPO, § 29 ZPO: Erfüllungsort des Arbeitsvertrags).
- Gütetermin within 2 Wochen (§ 54 ArbGG): aktive Vorbereitung auf Einigung; Abfindungsüberlegungen nach § 9, 10 KSchG.
- Kammertermin bei Nichteinigung (§ 57 ArbGG).

## Ausgabeformat

**Standardausgabe:** Rechtliches Memo im Gutachtenstil (vgl. references/methodik-buergerliches-recht.md Ziff. 6):
1. Sachverhalt
2. Frage
3. Ergebnis (1 Satz)
4. Rechtliche Bewertung (je Prüfungspunkt)
5. Gesamtergebnis und Empfehlung
6. Quellenverzeichnis

**Auf Anforderung:** Vollständige Klageschrift (Urteilsstil, Antrag + Begründung).

**Zusätzlich:** Checkliste Fristablauf und Anhörungsfehler als Tabelle.

## Beispiel

**Sachverhalt:** Arbeitnehmerin A ist seit 8 Jahren als Sachbearbeiterin bei der B-GmbH (85 Arbeitnehmer) beschäftigt. Am 15.04.2025 geht ihr eine ordentliche betriebsbedingte Kündigung zum 30.06.2025 zu. Ein Betriebsrat besteht. A behauptet, die B-GmbH habe die Sozialauswahl fehlerhaft durchgeführt, da die jüngere Kollegin K (3 Jahre Betriebszugehörigkeit, keine Unterhaltspflichten) trotz geringerer Sozialpunkte weiterbeschäftigt wurde.

**Frage:** Ist die Kündigung sozial gerechtfertigt?

**Ergebnis:** Die Kündigung dürfte sozial ungerechtfertigt sein, weil die Sozialauswahl fehlerhaft erscheint.

**Bewertung:**
*1. Geltungsbereich KSchG:* Die Wartezeit von 6 Monaten (§ 1 Abs. 1 KSchG) ist mit 8 Jahren erfüllt. Die Betriebsgröße von 85 Arbeitnehmern überschreitet den Schwellenwert des § 23 Abs. 1 KSchG. Das KSchG ist anwendbar.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Klagefrist:** Die 3-Wochen-Frist nach § 4 KSchG läuft bis zum 06.05.2025. Klage ist sofort einzureichen.

## Risiken und typische Fehler

| Risiko | Konsequenz | Gegenmittel |
|---|---|---|
| Fristversäumung § 4 KSchG | § 7 KSchG: Kündigung gilt als wirksam | Sofortprüfung Zugangsdatum; Klage vor Fristablauf einreichen |
| Kein Hinweis auf BR-Anhörungsfehler | Einwand geht verloren | Anhörungsunterlagen immer anfordern |
| KSchG nicht anwendbar (Kleinbetrieb) | Kein Kündigungsschutz nach § 1 KSchG | Betriebsgröße, allg. Schutz §§ 138, 242 BGB prüfen |
| Fehlende Abmahnung bei verhaltensbedingter Kündigung | Unverhältnismäßigkeit → Unwirksamkeit | Abmahnungshistorie vollständig aufklären |
| Versäumte 2-Wochen-Frist § 626 Abs. 2 BGB | Außerordentliche Kündigung unwirksam | Frist immer gesondert prüfen |
| Mandant ohne Anwalt im Gütetermin | Schlechte Verhandlungsposition | Anwaltliche Vertretung empfehlen (Kostenrisiko §§ 12a ArbGG) |
| Vertraulichkeit / § 203 StGB | Strafbarkeit bei unbefugter Datenweitergabe | Mandantendaten nur in zulässigen Systemen verarbeiten |
| Berufsrechtliche Pflichten (§ 43a BRAO) | Haftungs- und Berufsrechtsrisiko | Fristenkontrolle, Dokumentation, Belehrungspflichten |

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## DSGVO-Auskunft parallel zur KSchG-Klage

**Regelfall in der Praxis:** Arbeitnehmer und ihre Bevollmächtigten stellen häufig zeitgleich mit der KSchG-Klage oder unmittelbar nach Zugang der Kündigung ein Auskunftsersuchen nach Art. 15 DSGVO. Ziel ist der Zugang zu Personalakten, internen Vermerken, Abmahnungsunterlagen oder elektronischer Korrespondenz, die im Kündigungsschutzprozess als Beweismittel dienen oder den Arbeitgeber zu Verhandlungen über eine höhere Abfindung bewegen sollen.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Ein erstmaliges Auskunftsersuchen kann ausnahmsweise nach Art. 12 Abs. 5 S. 2 DSGVO als "exzessiv" eingestuft werden, wenn der Arbeitgeber sowohl ein **objektives Element** (z. B. ungewöhnlich kurzer Abstand zwischen Ausspruch der Kündigung und Auskunftsantrag; massenhaftes Legal-Tech-Vorgehen) als auch ein **subjektives Element** (missbräuchliche Absicht — Instrumentalisierung zur Schadensersatzgenerierung nach Art. 82 DSGVO statt Datenschutzschutz) nachweist. Die Hürden sind hoch; das Auskunftsrecht ist Grundrecht (Art. 8 GRCh).

**BAG-Linie zum immateriellen Schaden:**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Prozessuale Koordination:**
- Auskunftsklage nach Art. 15 DSGVO ist vor dem **Landgericht** einzuklagen (§ 44 BDSG i.V.m. Art. 79 DSGVO); das Arbeitsgericht ist nicht zuständig.
- Bei parallelem KSchG-Verfahren (Arbeitsgericht) und DSGVO-Auskunftsverfahren (Landgericht) Prozesstaktik koordinieren.
- Unberechtigte Ablehnung eines legitimen Auskunftsersuchens kann eigenständigen Schadensersatzanspruch nach Art. 82 DSGVO auslösen — auch ohne rechtswidrige Verarbeitung.
- Frist: Art. 12 Abs. 3 DSGVO — Antwort innerhalb eines Monats ab Eingang des Ersuchens; Verzögerung muss begründet und kommuniziert werden.

Querverweis: `arbeitsrecht/skills/kuendigungs-pruefung/SKILL.md` (Abschnitt DSGVO-Auskunftsersuchen als Druckmittel).

## Quellenpflicht

Jede juristische Aussage in jedem auf diesem Skill basierenden Dokument ist nach **references/zitierweise.md** zu belegen. Insbesondere:

- Rechtsprechungsbelege im BGH-Stil (Gericht, Entscheidungsform, Datum, Aktenzeichen, Fundstelle, Rn.).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Bei umstrittenen Fragen (z. B. Vergleichbarkeitsbegriff, Interessenabwägung) h. M. und Gegenauffassung getrennt zitieren.
- Halluzinationsrisiko: Alle Aktenzeichen und Fundstellen vor Einreichung gegenzuprüfen.
- Keine reine "vgl."-Floskel ohne nachvollziehbaren Verweis.
