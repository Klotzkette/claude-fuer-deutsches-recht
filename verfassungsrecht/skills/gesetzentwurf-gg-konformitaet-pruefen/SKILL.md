---
name: gesetzentwurf-gg-konformitaet-pruefen
description: "Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG Rechtsstaatsprinzip Verhältnismäßigkeit EU-Recht-Konformität. Output: Verfassun..."
---

# Gesetzentwurf — GG-Konformität prüfen (Gesetzgebersicht)

## Arbeitsbereich

Gesetzentwurf auf Grundgesetz-Konformität prüfen bevor Gesetzgebungsverfahren eingeleitet wird. Art. 1 20 GG Grundprinzipien Art. 70-80 GG Gesetzgebung. Prüfraster: formelle Verfassungsmäßigkeit Grundrechte Art. 20 GG Rechtsstaatsprinzip Verhältnismäßigkeit EU-Recht-Konformität. Output: Verfassungsprüfmemo Risikobewertung. Abgrenzung: nicht für laufende Normenkontrolle (normenkontrolle ist separates Plugin). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Gesetzentwurf — GG-Konformität prüfen (Gesetzgebersicht)
- **Normen-/Quellenanker:** GG, BVerfGG, VwGO/ZPO/StPO-Schnittstellen, Gesetzgebungskompetenz, Grundrechte, Verfassungsbeschwerde, konkrete/abstrakte Normenkontrolle.
- **Entscheidende Weiche:** Prüfe Beschwerdegegenstand, Beschwerdebefugnis, Rechtswegerschöpfung, Frist, Prüfungsmaßstab, Einschätzungsprärogative und Folgenabwägung.

## Disclaimer

Diese Prüfung dient der Gesetzgebungsvorbereitung in Ministerien und Regierungsstellen. Die verbindliche Klärung der Verfassungsmäßigkeit eines Gesetzes erfolgt im Streitfall ausschließlich durch das BVerfG (Art. 100 GG; Art. 93 Abs. 1 Nr. 2, 2a GG). Diese Prüfung ist eine Unterstützung und **kein Ersatz** für externe gutachterliche Beratung durch eine verfassungsrechtliche Spezialkanzlei.

## Quellenpflicht

Skill `bverfg-rechtsprechung-recherchieren` zuerst. Jede Aussage benötigt BVerfG-Pinpoint.

## Workflow

### Schritt 1 — Regelungsziel und Mittel bestimmen

- **Regelungsziel:** welcher Zustand soll erreicht / welche Gefahr abgewehrt werden?
- **Regelungsmittel:** welche Normen sollen erlassen werden?
- **Adressatenkreis:** wer wird betroffen?
- **Bestehende Regelungslage:** was gibt es bereits?

### Schritt 2 — Gesetzgebungskompetenz (Aufruf Skill `gesetzgebungskompetenz-pruefen`)

- Materiebestimmung (Schwerpunkt)
- Art. 70–74 GG durchgehen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Bei Abweichungsgesetzgebung Art. 72 Abs. 3 GG: Verhältnis Bund/Land klären.

### Schritt 3 — Formelle Verfassungsmäßigkeit (Aufruf Skill `formelle-verfassungsmaessigkeit`)

- Verfahren Art. 76–82 GG planen.
- **Zustimmungs- oder Einspruchsgesetz?** Prüfung früh, da Mehrheitsverhältnisse im Bundesrat berücksichtigt werden müssen.
- **Bestimmtheit:** Tatbestandsmerkmale, Rechtsfolgen, Zuständigkeiten klar regeln. Generalklauseln vermeiden, soweit Grundrechtsrelevanz hoch.
- **Zitiergebot Art. 19 Abs. 1 S. 2 GG:** Falls ein Grundrecht eingeschränkt wird, im Eingangsabschnitt das eingeschränkte Grundrecht unter Angabe des Artikels nennen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Schritt 4 — Materielle Verfassungsmäßigkeit pro betroffenes Grundrecht

Für jedes betroffene Grundrecht (Aufruf Skill `grundrechtspruefung`):

- Schutzbereich identifizieren.
- Eingriff bestimmen — auch mittelbare und faktische Eingriffe einbeziehen.
- Schranke benennen.
- **Schranken-Schranken** prüfen:
 - **Verhältnismäßigkeit** (Aufruf Skill `verhaeltnismaessigkeit`) — vier Stufen.
 - Wesensgehalt Art. 19 Abs. 2 GG.
 - Zitiergebot.
 - Allgemeinheit Art. 19 Abs. 1 S. 1 GG.
 - Wechselwirkungslehre bei Art. 5 Abs. 2 GG.
- Spezielle Strukturen einzelner Grundrechte berücksichtigen (Drei-Stufen-Theorie bei Art. 12 GG, Eingriffsformen bei Art. 14 GG, usw.).

### Schritt 5 — Sonstige verfassungsrechtliche Bindungen

#### 5a. Rechtsstaatsprinzip (Art. 20 Abs. 3 GG)

- **Bestimmtheitsgebot** (s. Schritt 3).
- **Vertrauensschutz und Rückwirkungsverbot:**
 - **Echte Rückwirkung** (Rückbewirkung von Rechtsfolgen) — grundsätzlich unzulässig.
 - **Unechte Rückwirkung** (tatbestandliche Rückanknüpfung) — zulässig, soweit Vertrauensschutz nicht überwiegt.
- **Faires Verfahren.**

#### 5b. Demokratieprinzip (Art. 20 Abs. 1, 2 GG)

- Lückenlose demokratische Legitimationskette für hoheitliches Handeln.
- Parlamentsvorbehalt (s. Wesentlichkeit).

#### 5c. Sozialstaatsprinzip (Art. 20 Abs. 1 GG)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Gleichmäßige Lastenverteilung.

#### 5d. Bundesstaatsprinzip (Art. 20 Abs. 1 GG)

- Beachtung der Länderkompetenzen.
- Bundestreue / Verfassungstreue.

#### 5e. Europarechtsfreundlichkeit

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Mit Unionsrecht vereinbar? Verstoß gegen Grundrechtecharta?

### Schritt 6 — Begründung des Entwurfs

Die Gesetzesbegründung sollte folgende Punkte zur Verfassungsmäßigkeit explizit ausführen:

1. **Gesetzgebungskompetenz** — einschlägige Norm benennen; bei Art. 72 Abs. 2 GG: Erforderlichkeit substantiiert dartun.
2. **Eingeschränkte Grundrechte** — explizit benennen, Zitiergebot wahren.
3. **Verhältnismäßigkeit** — Zweck, Geeignetheit, Erforderlichkeit, Angemessenheit pro Grundrecht durchargumentieren.
4. **Bezugnahme auf einschlägige BVerfG-Rechtsprechung** — Pinpoint mit Az. + Rn. + URL.
5. **Alternativen** — geprüfte mildere Mittel und Gründe für ihre Ablehnung.
6. **Folgenabschätzung** — auch zur Wahrung der Verhältnismäßigkeit.

### Schritt 7 — Risikoeinschätzung

- **Klassifikation:**
 - **Niedrig** — keine erkennbaren verfassungsrechtlichen Bedenken.
 - **Mittel** — auslegungsbedürftige Streitfragen; Stellungnahme aus Wissenschaft, Rechtsausschuss erwartbar.
 - **Hoch** — substantielle Bedenken; abstrakte Normenkontrolle oder Verfassungsbeschwerde wahrscheinlich.

- **Empfehlung bei mittlerem/hohem Risiko:** externe verfassungsrechtliche Begutachtung; Anpassungen am Entwurf, um Risiko zu reduzieren.

## Output-Format

```
GG-KONFORMITÄT GESETZENTWURF

Entwurf: ___
Regelungsziel: ___

1. Gesetzgebungskompetenz
 - Einschlägige Norm: Art. ___ GG
 - Bei Art. 72 Abs. 2 GG: Erforderlichkeit ___
 - BVerfG-Pinpoint: ___

2. Formelle Verfassungsmäßigkeit
 - Verfahren: ___
 - Zustimmungs-/Einspruchsgesetz: ___
 - Bestimmtheit: ___
 - Zitiergebot: ___
 - Wesentlichkeit (Kalkar): ___

3. Materielle Verfassungsmäßigkeit
 Pro betroffenes Grundrecht:
 - Art. ___ GG
 - Schutzbereich: ___
 - Eingriff: ___
 - Rechtfertigung: ___
 - Verhältnismäßigkeit: [4 Stufen]
 - BVerfG-Pinpoint: ___

4. Sonstige verfassungsrechtliche Bindungen
 - Rechtsstaat, Rückwirkung: ___
 - Demokratie / Parlamentsvorbehalt: ___
 - Sozialstaat: ___
 - Bundesstaat: ___
 - Unionsrecht: ___

5. Empfehlung Gesetzesbegründung
 - ___

6. Risikoeinschätzung
 - [niedrig / mittel / hoch]
 - Empfehlung: ___

BVerfG-Pinpoints
- ___
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Disclaimer-Wiederholung

Diese Prüfung ersetzt nicht die externe verfassungsrechtliche Begutachtung. Insbesondere die abschließende Beurteilung der Verfassungsmäßigkeit obliegt im Streitfall allein dem BVerfG.
