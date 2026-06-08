---
name: expansion-auftakt-fehlzeit-erfassen
description: "Expansion Auftakt Fehlzeit Erfassen im Plugin Arbeitsrecht: prüft konkret Startet die Planung einer Neueinstellung in einem weiteren, Neue Abwesenheit oder neuen Urlaubseintrag im Register, Überprüft offene Abwesenheiten und Fristen –, Entgeltfor. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Expansion Auftakt Fehlzeit Erfassen

## Arbeitsbereich

**Expansion Auftakt Fehlzeit Erfassen** ordnet den Fall über die tragenden Prüfungslinien: Startet die Planung einer Neueinstellung in einem weiteren, Neue Abwesenheit oder neuen Urlaubseintrag im Register, Überprüft offene Abwesenheiten und Fristen –. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `expansion-auftakt` | Startet die Planung einer Neueinstellung in einem weiteren Bundesland oder einem neuen Zielland — erhebt die relevanten Eckdaten, rahmt die Entscheidung AÜG-Modell / EOR / eigene Gesellschaft, entwirft abteilungsübergreifende Fragen und legt einen persistenten Tracker an. Lädt, wenn jemand sagt "wir stellen in [Land/Region] ein", "Expansion nach [Land]" oder "erste Einstellung in [Land]". |
| `fehlzeit-erfassen` | Neue Abwesenheit oder neuen Urlaubseintrag im Register anlegen – mit allen für die Fristenberechnung nach BUrlG, EFZG, MuSchG und BEEG notwendigen Informationen. Startet die Überwachung von Fristen ab dem ersten Tag. |
| `fehlzeiten-register` | Überprüft offene Abwesenheiten und Fristen – Urlaubsanspruch (BUrlG), Entgeltfortzahlung (EFZG), Mutterschutz (MuSchG), Elternzeit (BEEG). Zeigt nur Abwesenheiten, bei denen eine Entscheidung oder Handlung erforderlich ist – kein reines Statusboard. |
| `handbuch-aktualisierung` | Prüft eine geplante Änderung des Personalhandbuchs auf Folgewirkungen — andere betroffene Regelungen, standortspezifische Besonderheiten nach Tarifvertrag oder Betriebsvereinbarung, Mitbestimmungsrechte des Betriebsrats und die Frage, ob ein bestehendes Leistungsversprechen beschnitten wird. Lädt, wenn jemand sagt "Handbuch aktualisieren", "neue Regelung einpflegen" oder "Richtlinie ändern". |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `expansion-auftakt`

**Fokus:** Startet die Planung einer Neueinstellung in einem weiteren Bundesland oder einem neuen Zielland — erhebt die relevanten Eckdaten, rahmt die Entscheidung AÜG-Modell / EOR / eigene Gesellschaft, entwirft abteilungsübergreifende Fragen und legt einen persistenten Tracker an. Lädt, wenn jemand sagt "wir stellen in [Land/Region] ein", "Expansion nach [Land]" oder "erste Einstellung in [Land]".

# Expansions-Kickoff (Arbeitsrecht)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Expansions-Kickoff (Arbeitsrecht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Diese Skill startet ein strukturiertes Expansionsprojekt für eine neue
Einstellungsregion oder ein neues Land. Sie erhebt alle relevanten Ausgangsdaten,
erarbeitet die Entscheidungsgrundlage zwischen AÜG-Lösung/EOR und eigener
rechtlicher Einheit, formuliert die richtigen Fragen für Steuerberatung, Finanzen,
HR und externe Arbeitsrechtler und legt eine persistente Trackerdate an.

Die Skill setzt voraus, dass die Expansionsentscheidung grundsätzlich gefallen ist.
Sie ist kein Entscheidungsrahmen für "sollen wir überhaupt expandieren?".

Lädt, wenn eine Einstellung in einer neuen Jurisdiktion begonnen wird — typische
Auslöser: "erste Einstellung in Spanien", "Expansion nach Polen",
"brauchen wir eine GmbH in den Niederlanden?".

## Eingaben

- Zielland oder Zielbundesland
- Geplante Rollen / Stellenprofile
- Geplante Headcount-Zahl (12-Monats-Horizont)
- Wunschtermin für die erste Einstellung
- Bestehendes rechtliches Vehikel im Zielland (ja/nein)
- Strategische Stoßrichtung (Markteinstieg / langfristiger Aufbau)
- Entscheidungsträger auf Unternehmensseite (CFO, GF, HR-Leitung)

## Rechtlicher Rahmen

**Kernvorschriften:**

- §§ 611a, 613 BGB: Arbeitnehmereigenschaft, Unübertragbarkeit der Arbeitsleistung
- § 7 SGB IV: Beschäftigungsverhältnis, Scheinselbständigkeit
- §§ 1–19 AÜG: Arbeitnehmerüberlassungsgesetz — Erlaubnispflicht, Höchstüberlassungsdauer (§ 1 Abs. 1b AÜG: 18 Monate), Equal-Pay-Gebot (§ 8 AÜG)
- §§ 17, 18 KSchG: Massenentlassungsanzeige (relevant ab bestimmtem Schwellenwert)
- Art. 8 Rom I-VO: Arbeitsvertragsstatut bei grenzüberschreitenden Verhältnissen
- RL 2008/104/EG: Leiharbeits-Richtlinie

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- Arbeitnehmerstatus: § 611a BGB, § 7a SGB IV und frei verifizierte BAG-/BSG-Rechtsprechung; keine Kommentarzitate aus Modellwissen.
- AÜG: Erlaubnispflicht, Höchstüberlassungsdauer und Equal Pay nach Gesetz, Tariftext und frei verifizierter Rechtsprechung prüfen.
- AÜG/Equal Pay: Gesetz, Tariftext und freie Rechtsprechung nutzen; Fachliteratur nur mit Nutzerquelle.
- Grenzüberschreitende Arbeitsverhältnisse: Art. 8 Rom I-VO, AÜG, Entsende-/SV-Regeln und amtliche Quellen prüfen; keine Handbuchzitate aus Modellwissen.

## Ablauf

**Schritt 1 — Kontextladen**

Lese `CLAUDE.md` im Plugin-Verzeichnis → jurisdiktioneller Fußabdruck,
Eskalationstabelle, bestehende Expansionsnotizen.

**Schritt 2 — Prüfung bestehender Tracker**

Existiert bereits eine Tracker-Datei `expansion-[slug].yaml` für dieses Land?
Falls ja: "Für [Land] existiert bereits ein Expansions-Tracker. Nutzen Sie
`/arbeitsrecht:expansion-aktualisierung [Land]` für eine Aktualisierung oder bestätigen
Sie den Neustart."

**Schritt 3 — Strukturierte Informationserhebung**

Frage alle nachfolgenden Punkte in einem einzigen Block ab:

> Zur Erstellung des Expansionsplans werden folgende Angaben benötigt:
>
> **Die Expansion**
> - Welches Land / welches Bundesland?
> - Welche Rollen? (Stellenprofil ist entscheidend — ein Vertriebsmitarbeiter
> mit Abschlussvollmacht erzeugt anderes Risiko als eine Entwicklerstelle)
> - Wie viele Einstellungen im 12-Monats-Horizont?
> - Wann soll die erste Person starten?
>
> **Ausgangssituation**
> - Besteht bereits eine rechtliche Einheit im Zielland?
> - Wird ein EOR-Anbieter erwogen oder bereits genutzt?
> - Sind Steuerberatung und Finance bereits eingebunden?
> - Gibt es externe Arbeitsrechtler im Zielland?
>
> **Strategischer Kontext**
> - Langfristiger Aufbau oder Markttest (eine bis zwei Einstellungen)?
> - Wer ist der Entscheidungsträger für die Strukturentscheidung (GF, CFO)?

**Schritt 4 — Übergabe an `internationale-expansion`**

Lade die Referenz-Skill `internationale-expansion` und führe den vollständigen
Ablauf aus (Schritte 2–5).

**Schritt 5 — Tracker anlegen**

Lege `expansion-[slug].yaml` an und bestätige die Erstellung.

## Ausgabeformat

```
Expansions-Kickoff: [Land] — [Datum]

Erste Einstellung angestrebt: [Datum]
Headcount (12 Monate): [N]
Rollen: [Liste]
Tracker: expansion-[slug].yaml

EOR vs. Gesellschaft: [Einschätzung mit Fragen für Steuer/Finance]
Scheinselbständigkeitsrisiko: [Flag wenn zutreffend]

Offene Punkte ([N] gesamt):
| # | Punkt | Verantwortung | Status |
|---|---|---|---|
| 1 | ... | ... | Offen |
```

## Beispiel

```
/arbeitsrecht:expansion-auftakt Polen
```

```
/arbeitsrecht:expansion-auftakt
(Skill fragt nach dem Zielland)
```

Ausgabe bei Einstellung von zwei Vertriebsmitarbeitern in Polen:

> PE-Risiko: Vertriebsrollen mit Abschlussbefugnis können auch ohne
> polnische GmbH eine steuerliche Betriebsstätte begründen. Frage an
> Steuerberatung vor der ersten Einstellung klären.

## Risiken und typische Fehler

- **Scheinselbständigkeit § 7 SGB IV**: Freie Mitarbeiter im Ausland, die
 faktisch weisungsgebunden und eingegliedert sind, gelten als Arbeitnehmer.
 Nachzahlungsrisiko Sozialversicherung bis zu vier Jahre rückwirkend.
- **AÜG-Falle bei EOR**: Wird ein EOR ohne AÜG-Erlaubnis genutzt und liegt
 echte Arbeitnehmerüberlassung vor, kann kraft Gesetzes ein Arbeitsverhältnis
 zum Entleiher entstehen (§ 10 Abs. 1 AÜG).
- **18-Monats-Grenze**: Die gesetzliche Höchstüberlassungsdauer beträgt
 18 Monate (§ 1 Abs. 1b AÜG). Überschreitung ohne tarifvertragliche Ausnahme
 ist bußgeldbewehrt.
- **Fehlende Vorabklärung Betriebsstättenrisiko**: Vertriebsmitarbeiter mit
 Vertretungsmacht können in vielen Ländern steuerlich eine Betriebsstätte
 begründen — Steuerberatung vor Einstellungsbeginn zwingend.
- **Arbeitsvertrag nach dem Recht des Stammlandes**: Art. 8 Rom I-VO schützt
 Arbeitnehmer vor Abwahl zwingender Schutzvorschriften des
 Beschäftigungsstaats. Reine Rechtswahl zugunsten deutschen Rechts schützt
 nicht vor Mindeststandards des Einsatzlandes.

## Quellenpflicht

Jede Ausgabe dieser Skill muss bei Structural-Empfehlungen zitieren:

- § 7 SGB IV (Scheinselbständigkeit), §§ 1, 8, 10 AÜG
- Art. 8 Rom I-VO bei grenzüberschreitenden Konstellationen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- AÜG: Erlaubnispflicht, Höchstüberlassungsdauer und Equal Pay nach Gesetz, Tariftext und frei verifizierter Rechtsprechung prüfen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## 2. `fehlzeit-erfassen`

**Fokus:** Neue Abwesenheit oder neuen Urlaubseintrag im Register anlegen – mit allen für die Fristenberechnung nach BUrlG, EFZG, MuSchG und BEEG notwendigen Informationen. Startet die Überwachung von Fristen ab dem ersten Tag.

# /arbeitsrecht:fehlzeit-erfassen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:fehlzeit-erfassen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Neue Abwesenheit in `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/urlaubsregister.yaml` eintragen, sodass der Urlaub-/Fehlzeiten-Tracker alle Fristen ab Tag 1 überwacht.

## Eingaben

- Mitarbeiter-Angaben (Name/ID – anonymisiert genügt)
- Abwesenheitstyp und Startdatum
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Standort, Tarifvertrag

## Ablauf

### 1. Konfiguration lesen

Standort-Fußabdruck, HRIS-Status, Tarifvertrag prüfen. Falls HRIS verbunden: Hinweis, dass Eintrag besser dort erfolgt; trotzdem im Register dokumentieren, wenn Nutzer dies wünscht.

### 2. Alle nötigen Informationen in einem einzigen Prompt abfragen

> Kurze Angaben für den Fehlzeiteintrag:
>
> - **Mitarbeiter-ID oder Rolle** (anonymisiert ist in Ordnung)
> - **Bundesland** (bestimmt anwendbare Regeln)
> - **Abwesenheitstyp:**
> - Krankheit / Arbeitsunfähigkeit (EFZG)
> - Urlaub (BUrlG)
> - Mutterschutz / Beschäftigungsverbot (MuSchG)
> - Elternzeit (BEEG)
> - Pflegezeit (PflegeZG)
> - Sonstiges
> - **Startdatum** der Abwesenheit
> - **Voraussichtliches Rückkehrdatum** (falls bekannt – leer lassen wenn unbekannt)
> - **Bei Elternzeit:** Hat die Mitarbeiterin/der Mitarbeiter die Elternzeit schriftlich angemeldet? Anmeldedatum?
> - **Bei Krankheit:** Gleiche Erkrankung wie in zurückliegenden 12 Monaten? (für EFZG-Neuanspruchs-Berechnung)
> - **Schwangerschaft/Entbindung:** Errechneter Entbindungstermin (für MuSchG-Fristen)

### 3. Fristen automatisch berechnen

Je nach Abwesenheitstyp:

**Krankheit (EFZG):**
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BEM-Prüfdatum: ab 6-wöchiger AU innerhalb von 12 Monaten (§ 167 Abs. 2 SGB IX)
- Wenn gleiche Erkrankung: Neuer EFZG-Anspruch? Letzter AU-Zeitraum prüfen.

**Urlaub (BUrlG):**
- Verfallsdatum: 31.12. des laufenden Jahres (§ 7 Abs. 3 S. 1 BUrlG) bzw. 31.03. des Folgejahres bei Übertragung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Resturlaub berechnen: Gesamtanspruch − genommene Tage

**Mutterschutz (MuSchG):**
- Schutzfrist-Beginn: 6 Wochen vor errechnetem Entbindungstermin (§ 3 MuSchG)
- Schutzfrist-Ende: 8 Wochen nach Entbindung (§ 3 Abs. 2 MuSchG; 12 Wochen bei Frühgeburt)
- Kündigungsschutz-Ende: 4 Monate nach Entbindung (§ 17 Abs. 1 S. 1 Nr. 1 MuSchG)

**Elternzeit (BEEG):**
- Anmeldefrist geprüft? (7 Wochen vor Beginn; § 16 Abs. 1 BEEG)
- Elternzeit-Ende: 3. Geburtstag des Kindes als maximale Frist
- Kündigungsschutz-Ende: Ende der Elternzeit (§ 18 Abs. 1 BEEG)
- Teilzeit-Anspruch: Ab Beginn der Elternzeit (§ 15 Abs. 6 BEEG)

**Pflegezeit (PflegeZG):**
- Max. 6 Monate (§ 3 Abs. 1 PflegeZG)
- Kündigungsschutz: ab Ankündigung bis 4 Wochen nach Ende (§ 5 PflegeZG)
- Ankündigungsfrist: 10 Arbeitstage vor Beginn (§ 3 Abs. 3 PflegeZG)

### 4. Eintrag schreiben

Register-Eintrag anlegen in `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/urlaubsregister.yaml`:

```yaml
- id: [generierte ID]
 mitarbeiter: [anonymisierte Bezeichnung]
 bundesland: [BL]
 typ: [krankheit|urlaub|mutterschutz|elternzeit|pflegezeit|sonstiges]
 startdatum: [JJJJ-MM-TT]
 rueckkehr_geplant: [JJJJ-MM-TT | unbekannt]
 fristen:
 efzg_erschoepfung: [JJJJ-MM-TT] # nur bei Krankheit
 bem_pruefung: [JJJJ-MM-TT] # nur bei Krankheit ≥ 6 Wochen
 urlaubsverfall_warnung: [JJJJ-MM-TT] # nur bei Urlaub
 schutzfrist_ende: [JJJJ-MM-TT] # MuSchG/BEEG
 ks_schutz_ende: [JJJJ-MM-TT] # Kündigungsschutz-Ende
 notizen: [ggf.]
 status: offen
```

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

- § 3 EFZG (6-Wochen-Fortzahlung), § 5 EFZG (Nachweispflicht)
- § 3, 7 BUrlG (Mindesturlaub, Übertragung, Verfall)
- § 3 MuSchG (Schutzfristen), § 17 MuSchG (Kündigungsschutz)
- §§ 15–18 BEEG (Elternzeit, Anmeldung, Kündigungsschutz)
- § 167 Abs. 2 SGB IX (BEM-Pflicht)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
FEHLZEITEINTRAG ANGELEGT – [ID] – [Datum]

Mitarbeiter: [ID/Rolle]
Typ: [Abwesenheitstyp]
Bundesland: [BL]
Start: [Datum]
Rückkehr: [Datum / unbekannt]

Berechnete Fristen:
 [Fristname]: [Datum] [Norm]

Gespeichert: ~/.../urlaubsregister.yaml
Nächste Prüfung: /arbeitsrecht:fehlzeiten-register
```

## Beispiele

```
/arbeitsrecht:fehlzeit-erfassen
Mitarbeiterin HR-022, Bayern, Elternzeit ab 01.02.2025.
Anmeldung liegt schriftlich vor (10.12.2024). Rückkehr geplant 01.02.2026.
```

## Risiken / typische Fehler

- **BEEG-Anmeldung nachträglich** – Elternzeit kann nicht rückwirkend beantragt werden; Anmeldedatum prüfen.
- **Mehrere Abwesenheitsperioden bei gleicher Erkrankung** – EFZG-Neuanspruch-Prüfung nicht vergessen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Anonymisierung** – auch im internen Register: Mitarbeiter-IDs statt Namen verwenden; § 26 BDSG.

## 3. `fehlzeiten-register`

**Fokus:** Überprüft offene Abwesenheiten und Fristen – Urlaubsanspruch (BUrlG), Entgeltfortzahlung (EFZG), Mutterschutz (MuSchG), Elternzeit (BEEG). Zeigt nur Abwesenheiten, bei denen eine Entscheidung oder Handlung erforderlich ist – kein reines Statusboard.

# /arbeitsrecht:fehlzeiten-register

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:fehlzeiten-register` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Dieser Skill überprüft alle offenen Abwesenheiten mit gesetzlichen Fristen und zeigt nur diejenigen, bei denen eine Entscheidung oder Handlung erforderlich ist. Er ist kein Statusboard – er teilt Ihnen mit, was Sie tun müssen und warum.

## Eingaben

- HRIS-Zugang (falls konfiguriert) oder `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/urlaubsregister.yaml`
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Standort, Tarifvertrag, Betriebsvereinbarungen

## Ablauf

### 1. Datenquelle ermitteln

Falls HRIS verbunden: Abwesenheitsdaten abrufen. Falls nicht: `urlaubsregister.yaml` lesen. Falls beides fehlt: "Kein Urlaubsregister gefunden. Bitte HRIS verknüpfen oder Abwesenheiten über `/arbeitsrecht:fehlzeit-erfassen` eintragen."

### 2. Fristen-Check für jede offene Abwesenheit

**A – Urlaub (BUrlG):**
- Gesetzlicher Mindesturlaub: 20 Werktage (§ 3 Abs. 1 BUrlG bei 5-Tage-Woche) bzw. 24 Werktage (§ 3 Abs. 1 BUrlG bei 6-Tage-Woche)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wartefrist:** Voller Urlaubsanspruch erst nach 6-monatigem Bestehen (§ 4 BUrlG); vorher anteiliger Anspruch (§ 5 BUrlG)
- **Urlaubsabgeltung** bei Beendigung des Arbeitsverhältnisses (§ 7 Abs. 4 BUrlG); steuer- und sozialversicherungspflichtig

**B – Entgeltfortzahlung (EFZG):**
- 6-Wochen-Frist pro Erkrankung (§ 3 Abs. 1 EFZG)
- **Beginn neuer Anspruch bei gleicher Krankheit:** Erst nach 6-monatiger Unterbrechung oder 12-Monats-Zeitraum seit letzter AU (§ 3 Abs. 1 S. 2 EFZG)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wiedereingliederung (stufenweise):** § 74 SGB V, § 28 SGB IX; Anspruch auf Zustimmung zur stufenweisen Wiedereingliederung

**C – Mutterschutz (MuSchG):**
- **Beschäftigungsverbote** (§§ 3–6 MuSchG): 6 Wochen vor dem errechneten Entbindungstermin (§ 3 MuSchG), 8 Wochen nach der Entbindung (§ 3 Abs. 2 MuSchG; bei Frühgeburten: 12 Wochen)
- **Kündigungsschutz** (§ 17 MuSchG): Während Schwangerschaft bis 4 Monate nach Entbindung; Ausnahme nur mit behördlicher Genehmigung
- **Mutterschaftsgeld:** Kassenleistung; Arbeitgeberanteil über Arbeitgeberzuschuss (§ 20 MuSchG)
- **Fristen im Tracker:** Errechneter Entbindungstermin → Fristberechnung Schutzfrist-Ende; Mitteilungspflicht Arbeitnehmer § 15 MuSchG

**D – Elternzeit (BEEG):**
- Anspruch bis 3 Jahre je Kind (§ 15 Abs. 2 BEEG); 24 Monate zwischen 3. und 8. Geburtstag
- **Anmeldefrist:** 7 Wochen vor Beginn (§ 16 Abs. 1 BEEG); bei Elternzeit ab Geburt: 7 Wochen vor Beginn; kann nicht rückwirkend genommen werden
- **Kündigungsschutz** (§ 18 BEEG): Ab Anmeldung der Elternzeit bis zum Ende; Ausnahme § 18 Abs. 1 S. 2 BEEG (besondere Fälle)
- **Teilzeit in Elternzeit** (§ 15 Abs. 6–7 BEEG): Bis 30 h/Woche; Arbeitgeber kann nur bei dringenden betrieblichen Gründen ablehnen
- **Elterngeld:** BEEG §§ 1–13 – keine arbeitsrechtliche Pflicht des Arbeitgebers, aber Informationspflicht

### 3. Alerts nur bei Handlungsbedarf

Darstellung:
- 🔴 **Sofortmaßnahme:** Frist in < 7 Tagen
- 🟠 **Zeitnah handeln:** Frist in 7–30 Tagen
- 🟡 **Auf dem Radar:** Frist in 30–90 Tagen
- 🟢 **Unauffällig** – kein Handlungsbedarf

Keine langen Statustabellen – nur Fälle mit Handlungsbedarf, jeweils mit einem Satz: Wer, was, bis wann.

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Wesentliche Quellen:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

```
URLAUB- UND FEHLZEITEN-TRACKER – [Datum]

Aktive Abwesenheiten: [N gesamt] | Handlungsbedarf: [N]

🔴 SOFORTMASSNAHME
 [Name/ID] – [Abwesenheitstyp] – Frist: [Datum]
 → [Was zu tun ist, in einem Satz]

🟠 ZEITNAH HANDELN
 [Name/ID] – [Typ] – Frist: [Datum]
 → [Handlung]

🟢 Unauffällig ([N] Fälle)
 [kurze Zusammenfassung, eine Zeile]

Wie weiter? [Entscheidungsbaum]
```

## Beispiele

```
/arbeitsrecht:fehlzeiten-register
```

```
URLAUB- UND FEHLZEITEN-TRACKER – 15.01.2025

Aktive Abwesenheiten: 8 gesamt | Handlungsbedarf: 2

🟠 ZEITNAH HANDELN
 MA-0047 (Projektmanagerin) – Elternzeit-Anmeldung – Frist: 03.02.2025
 → Elternzeitanmeldung mit 7-Wochen-Frist (§ 16 Abs. 1 BEEG) liegt noch nicht vor.
 Bitte Mitarbeiterin erinnern und Antrag schriftlich bestätigen.

🟡 AUF DEM RADAR
 MA-0031 (Vertrieb) – EFZG-Erschöpfung (gleiche Erkrankung) – 05.03.2025
 → 6. Krankheitswoche bei derselben Erkrankung. BEM prüfen (§ 167 Abs. 2 SGB IX).
 EFZG-Anspruch erschöpft sich am 05.03.2025.

🟢 Unauffällig (6 Fälle) – keine Handlung erforderlich.
```

## Risiken / typische Fehler

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **BEEG-Anmeldefrist verpasst** – Elternzeit kann nicht rückwirkend genommen werden; späteste Anmeldung 7 Wochen vor Beginn.
- **BEM-Pflicht vor Kündigung** – ohne BEM erhöhte Darlegungslast des Arbeitgebers bei krankheitsbedingter Kündigung.
- **Mutterschutzfristen falsch berechnet** – bei Mehrlingsbirth oder Frühgeburt gelten abweichende Schutzfristen (§ 3 Abs. 2 S. 2 MuSchG: 12 Wochen statt 8 Wochen).

## 4. `handbuch-aktualisierung`

**Fokus:** Prüft eine geplante Änderung des Personalhandbuchs auf Folgewirkungen — andere betroffene Regelungen, standortspezifische Besonderheiten nach Tarifvertrag oder Betriebsvereinbarung, Mitbestimmungsrechte des Betriebsrats und die Frage, ob ein bestehendes Leistungsversprechen beschnitten wird. Lädt, wenn jemand sagt "Handbuch aktualisieren", "neue Regelung einpflegen" oder "Richtlinie ändern".

# Personalhandbuch-Aktualisierung (Arbeitsrecht)

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Personalhandbuch-Aktualisierung (Arbeitsrecht)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Änderungen am Personalhandbuch haben Folgewirkungen. Eine geänderte
Urlaubsregelung betrifft die Berechnung der Urlaubsabgeltung bei Beendigung,
die Verweisklauseln in anderen Abschnitten und ggf. bestehende
Betriebsvereinbarungen zum Thema. Diese Skill findet die Folgewirkungen,
bevor sie zu Widersprüchen werden.

Lädt, wenn eine Regelungsänderung im Personalhandbuch vorbereitet wird und
Folgewirkungen systematisch geprüft werden sollen.

## Eingaben

- Betroffener Abschnitt des Personalhandbuchs
- Neuer Regelungstext (Entwurf)
- Grund der Änderung (gesetzliche Anforderung, Unternehmensentscheidung, Bereinigung)
- Jurisdiktioneller Fußabdruck des Unternehmens (Standorte, Tarifbindung)
- Bestehende Betriebsvereinbarungen zum Thema (falls bekannt)

## Rechtlicher Rahmen

**Kernvorschriften:**

- § 87 BetrVG: Erzwingbares Mitbestimmungsrecht des Betriebsrats bei
 Ordnung des Betriebs, Arbeitszeit, Urlaub, betrieblichem Datenschutz u. a.
 — Handbuchänderungen in diesen Bereichen erfordern Betriebsratszustimmung
 oder Einigungsstellenverfahren
- § 77 BetrVG: Betriebsvereinbarungen — Vorrang und Ablösung;
 Nachwirkung gekündigter Betriebsvereinbarungen (§ 77 Abs. 6 BetrVG)
- §§ 305 ff. BGB: AGB-Kontrolle für vorformulierte Arbeitsbedingungen;
 Inhaltskontrolle nach § 307 BGB; Transparenzgebot § 307 Abs. 1 S. 2 BGB
- § 2 NachwG: Nachweispflicht wesentlicher Arbeitsbedingungen;
 Änderungen sind dem Arbeitnehmer spätestens am ersten Tag nach Wirksamwerden
 schriftlich mitzuteilen
- §§ 611a, 613 BGB: Arbeitsvertragliche Einbindung von Handbuchregelungen
 durch Bezugnahmeklauseln

**Leitentscheidungen:**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Wirksame Einbeziehung von Personalhandbuch-Regelungen durch Bezugnahmeklausel
 im Arbeitsvertrag; AGB-Kontrolle; Maßstab der überraschenden Klausel
 nach § 305c Abs. 1 BGB
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Verschlechterung einer durch betriebliche Übung entstandenen
 Leistungsverpflichtung — einseitige Abänderung unwirksam; Änderungskündigung
 als richtiger Weg; Vertrauensschutz der Arbeitnehmer
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Mitbestimmung des Betriebsrats bei einseitiger Änderung betrieblicher
 Regelungen, die in den Bereich des § 87 BetrVG fallen; Einigungsstellenverfahren

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 Katalog erzwingbarer Mitbestimmungsrechte; Reichweite der Mitbestimmung
 bei Regelungsänderungen
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 AGB-Kontrolle vorformulierter Arbeitsbedingungen; Inhaltskontrolle
 und Transparenzgebot im Arbeitsverhältnis
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 Nachweispflicht bei Änderungen wesentlicher Arbeitsbedingungen,
 Formerfordernis und Folgen der Verletzung

## Ablauf

**Schritt 1 — Änderung erfassen**

- Welcher Abschnitt wird geändert?
- Was ist der neue Wortlaut?
- Warum? (Gesetzliche Anforderung, Unternehmensentscheidung, Bereinigung)

**Schritt 2 — Vergleich mit dem aktuellen Stand**

Zeige den Vergleich:

```diff
- [bisheriger Wortlaut]
+ [neuer Wortlaut]
```

**Schritt 3 — Querverweise prüfen**

Durchsuche das Personalhandbuch nach Bezügen auf den geänderten Abschnitt:

- Andere Regelungen, die auf diesen Abschnitt verweisen
 ("zur Urlaubsabgeltung siehe Abschnitt …")
- Definierte Begriffe, die dieser Abschnitt verwendet oder definiert
- Standort- oder tarifvertragliche Sonderregelungen, die diesen Abschnitt
 modifizieren

Für jeden Querverweis: Gilt er nach der Änderung noch unverändert?
Wird er durch die Änderung falsch oder unvollständig? Kennzeichne Konflikte.

**Schritt 4 — Mitbestimmungsprüfung**

Prüfe, ob die geplante Änderung in den Bereich eines Mitbestimmungstatbestands
nach § 87 BetrVG fällt (insbesondere Nr. 1 Ordnung des Betriebs, Nr. 2/3
Arbeitszeit, Nr. 5 Urlaub, Nr. 6 Überwachungstechnik, Nr. 10
Entlohnungsgrundsätze). Falls ja:

> Mitbestimmungshinweis: Diese Änderung berührt [Tatbestand § 87 Abs. 1
> Nr. X BetrVG]. Eine wirksame Einführung ohne Zustimmung des Betriebsrats
> ist nicht möglich. Optionen: (1) Zustimmung des Betriebsrats einholen,
> (2) Einigungsstellenverfahren nach § 76 BetrVG.

**Schritt 5 — Prüfung standortspezifischer Besonderheiten**

Prüfe für jeden Standort im Fußabdruck:
- Modifiziert eine bestehende Betriebsvereinbarung diesen Bereich?
- Macht die Änderung eine bestehende Betriebsvereinbarung obsolet, falsch
 oder unvollständig?
- Entsteht für einen Standort erstmals Anpassungsbedarf?

**Schritt 6 — Leistungsversprechen-Check**

Wird durch die Änderung eine bislang gewährte Leistung reduziert oder gestrichen?

Falls ja: Risikokennzeichnung. In der Rechtsprechung können Handbuchregelungen
als vertragliche Vereinbarung oder betriebliche Übung bindend sein
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
eine Änderungskündigung oder eine Mitarbeiterinformation mit Zustimmungserfordernis
erfordern. Nicht blockieren — kennzeichnen.

**Schritt 7 — Nachweispflicht**

Prüfe, ob die geänderte Regelung eine "wesentliche Arbeitsbedingung" i. S. d.
§ 2 Abs. 1 NachwG darstellt. Falls ja: Informationspflicht gegenüber den
betroffenen Arbeitnehmern spätestens am Tag nach Wirksamwerden.

## Ausgabeformat

```markdown
## Handbuchänderung: [Abschnitt]

### Änderung
[diff]

### Querverweis-Auswirkungen
| Abschnitt | Bezug zur Änderung | Noch korrekt? | Handlungsbedarf |
|---|---|---|---|
| [Name] | [wie] | Ja/Nein | [was] |

### Mitbestimmung
[Falls § 87 BetrVG betroffen: Tatbestand und erforderliches Vorgehen]
[Falls nicht betroffen: "Kein erzwingbares Mitbestimmungsrecht betroffen"]

### Standortspezifische Auswirkungen
| Standort | Bestehende Betriebsvereinbarung | Nach Änderung | Maßnahme |
|---|---|---|---|
| [Standort] | [Inhalt] | [weiter gültig / obsolet / anzupassen] | [keine / Update / neu] |

### Leistungsversprechen-Check
[Falls Leistungsreduzierung: Kennzeichnung + rechtliche Risikoeinschätzung]

### Nachweispflicht
[Falls § 2 NachwG betroffen: Information an Arbeitnehmer erforderlich]

### Freigabe-Checkliste
- [ ] Querverweise angepasst
- [ ] Betriebsvereinbarungen aktualisiert (falls erforderlich)
- [ ] Betriebsrat involviert (falls § 87 BetrVG betroffen)
- [ ] Leistungsversprechen-Frage geklärt (falls Reduzierung)
- [ ] Versionsnummer und Datum aktualisiert
- [ ] Mitarbeiterinformation gemäß § 2 NachwG (falls erforderlich)
```

## Beispiel

Szenario: Das Unternehmen möchte die Urlaubsregelung von 30 auf 25 Werktage
Jahresurlaub (bei einer 5-Tage-Woche) reduzieren. Die Regelung war im
Personalhandbuch niedergelegt und wurde seit drei Jahren allen Einstellungen
versprochen.

Ausgabe der Skill:

> Leistungsversprechen-Check: Die Reduzierung des Jahresurlaubs unterschreitet
> den bisher im Handbuch versprochenen Wert. Sofern die 30-Tage-Regelung durch
> betriebliche Übung (§ 611a BGB i. V. m. Grundsatz der betrieblichen Übung)
> oder vertragliche Bezugnahme bindend ist, bedarf die Änderung entweder der
> individuellen Zustimmung jedes betroffenen Arbeitnehmers oder einer
> Änderungskündigung (§§ 2, 4 KSchG). Mitbestimmung des Betriebsrats nach
> § 87 Abs. 1 Nr. 5 BetrVG ist zu prüfen.

## Risiken und typische Fehler

- **Mitbestimmung vergessen**: Änderungen in Bereichen des § 87 BetrVG
 ohne Betriebsratsinhaber sind unwirksam — auch wenn sie sachlich gerechtfertigt sind.
- **Betriebliche Übung unterschätzt**: Was über Jahre konsistent gewährt wurde,
 kann bindend sein — auch ohne ausdrücklichen Vertrag.
- **NachwG-Frist versäumt**: Änderungen wesentlicher Arbeitsbedingungen müssen
 spätestens am nächsten Arbeitstag schriftlich mitgeteilt werden.
- **AGB-Kontrolle nicht geprüft**: Vorformulierte Handbuchklauseln unterliegen
 §§ 305 ff. BGB; überraschende oder unangemessen belastende Klauseln sind
 unwirksam.
- **Standortspezifika übersehen**: Betriebsvereinbarungen an einzelnen
 Standorten können bundesweite Handbuchregelungen einschränken oder erweitern.

## Quellenpflicht

Jede Ausgabe dieser Skill muss bei mitbestimmungsrelevanten Änderungen zitieren:

- § 87 BetrVG (Mitbestimmungstatbestand), § 77 BetrVG (Betriebsvereinbarung)
- § 2 NachwG (Nachweispflicht)
- §§ 305 ff. BGB (AGB-Kontrolle)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 87 Abs. 1 Nr. 6 BetrVG: Mitbestimmung bei technischen Überwachungseinrichtungen; Rechtsprechung nur frei verifiziert zitieren.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
