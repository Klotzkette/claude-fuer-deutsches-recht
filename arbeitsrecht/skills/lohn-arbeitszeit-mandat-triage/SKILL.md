---
name: lohn-arbeitszeit-mandat-triage
description: "Lohn Arbeitszeit Mandat Triage im Plugin Arbeitsrecht: prüft konkret Standortbezogene Lohn- und Arbeitszeitfragen – ArbZG, Pausen, Eingangs-Abfrage für arbeitsrechtliche Mandate — Mandant, Prüfungslinie für massenentlassung 17 kschg. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Lohn Arbeitszeit Mandat Triage

## Arbeitsbereich

**Lohn Arbeitszeit Mandat Triage** ordnet den Fall über die tragenden Prüfungslinien: Standortbezogene Lohn- und Arbeitszeitfragen – ArbZG, Pausen, Eingangs-Abfrage für arbeitsrechtliche Mandate — Mandant. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `lohn-arbeitszeit-fragen` | Standortbezogene Lohn- und Arbeitszeitfragen – ArbZG (Höchstarbeitszeit, Pausen, Ruhezeiten, Aufzeichnungspflichten), MiLoG (Mindestlohn, Aufzeichnungspflicht), EFZG (Entgeltfortzahlung im Krankheitsfall), Tarifverträge, Überstunden. Antwort mit der maßgeblichen Norm und Zitat. |
| `mandat-triage-arbeitsrecht` | Eingangs-Abfrage für arbeitsrechtliche Mandate — Mandant fragt nach Kündigung Aufhebungsvertrag Abmahnung Lohn Urlaub Befristung Betriebsuebergang Diskriminierung oder Betriebsrats-Streit. Klaert Mandantenrolle (Arbeitnehmer Arbeitgeber Betriebsrat Geschäftsführer). Sofort-Fristen-Check § 4 KSchG drei Wochen Kündigungsschutzklage § 17 TzBfG drei Wochen Entfristung. Normen § 1 KSchG § 611a BGB § 102 BetrVG § 17 KSchG Massenentlassung. Eskalation Telefon-Sofort bei Kündigung mit drohender Klagefrist Massenentlassung Betriebsuebergang. Output Triage-Memo mit Fristen-Ampel und Routing zu kündigungs-prüfung betriebsrat-anhoerung oder entfristung-Skills. Abgrenzung zu mandat-arbeitsbereich (Workspace-Verwaltung). |
| `massenentlassung-17-kschg` | Prüfungslinie für massenentlassung 17 kschg: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `mindestlohn-arbeitszeit-erfassung` | Prüfungslinie für mindestlohn arbeitszeit erfassung: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `lohn-arbeitszeit-fragen`

**Fokus:** Standortbezogene Lohn- und Arbeitszeitfragen – ArbZG (Höchstarbeitszeit, Pausen, Ruhezeiten, Aufzeichnungspflichten), MiLoG (Mindestlohn, Aufzeichnungspflicht), EFZG (Entgeltfortzahlung im Krankheitsfall), Tarifverträge, Überstunden. Antwort mit der maßgeblichen Norm und Zitat.

### /arbeitsrecht:lohn-arbeitszeit-fragen

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `/arbeitsrecht:lohn-arbeitszeit-fragen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

"Es kommt darauf an" ist wahr, aber keine nützliche Antwort. Dieser Skill liefert standortspezifische Antworten mit der maßgeblichen Norm, zitiert und mit Kennzeichnung von Grenzfällen.

## Eingaben

- Konkrete Frage (Freitext)
- Jurisdiktion / Bundesland (falls nicht aus Profil erkennbar)
- Tätigkeit / Branche (für Tarifverträge)
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` → Standort, Tarifbindung, Arbeitszeitmodelle

## Ablauf

### 1. Jurisdiktion und Tarifbindung klären

Falls aus dem Profil erkennbar: direkt verwenden. Andernfalls fragen. Prüfen:
- Gilt ein Tarifvertrag? (Tariflich abweichende Regelungen bei ArbZG §§ 7, 12 möglich)
- Existiert eine Betriebsvereinbarung zu Arbeitszeit/Vergütung?
- Branchenspezifische Mindestlöhne (§ 7 AEntG, z.B. Bau, Pflege, Gebäudereinigung, Sicherheit)?

### 2. ArbZG-Prüfung (Arbeitszeitgesetz)

**Gesetzliche Höchstgrenzen (§§ 3–5 ArbZG):**
- Täglich max. 8 Stunden (Werktage), verlängerbar auf max. 10 Stunden, wenn Ausgleich in 6 Monaten auf 8 h/Tag im Durchschnitt (§ 3 S. 2 ArbZG)
- **Pausen:** Bei 6–9 Stunden: 30 Minuten; bei > 9 Stunden: 45 Minuten (§ 4 ArbZG). Aufteilung in Blöcke ≥ 15 Minuten möglich.
- **Ruhezeit:** Min. 11 Stunden nach Ende der Arbeitszeit (§ 5 ArbZG)
- **Wochenarbeitszeit:** Keine direkte gesetzliche Begrenzung, aber durch Tageshöchstgrenze × 6 Werktage de facto max. 48–60 h

**Sonderregelungen:**
- § 7 ArbZG: Tarifvertragliche Verlängerungen möglich (z.B. auf 12 h täglich bei Bereitschaftsdienst)
- § 10 ArbZG: Sonn- und Feiertagsarbeit verboten (Ausnahmen §§ 10–13 ArbZG); Ersatzruhetag innerhalb 8 Wochen (§ 11 Abs. 3 ArbZG)
- § 18 ArbZG: Nicht anwendbar auf leitende Angestellte i.S.d. § 5 Abs. 3 BetrVG

**Arbeitszeiterfassung:**
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 3. MiLoG (Mindestlohngesetz)

**Aktueller Mindestlohn:** § 1 Abs. 2 MiLoG. Werte (Quelle: Bundeskabinett, Mindestlohnanpassungsverordnungen; BMAS):
- 01.01.2024: EUR 12,41 / Stunde
- 01.01.2025: EUR 12,82 / Stunde
- **01.01.2026: EUR 13,90 / Stunde** (Fuenfte Mindestlohnanpassungsverordnung)
- 01.01.2027 (vorgesehen): EUR 14,60 / Stunde

Anpassung durch Mindestlohnkommission gem. § 9 MiLoG; Umsetzung durch Verordnung des BMAS. Vor jedem Schriftsatz oder jeder Beratung aktuellen Wert in bundesregierung.de / bmas.de pruefen.

Hinweis: Die Minijob-Verdienstgrenze ist an den Mindestlohn gekoppelt; sie betraegt zum 01.01.2026 EUR 603 / Monat (Quelle: Deutsche Rentenversicherung Baden-Wuerttemberg, Pressemitteilung 22.12.2025).

**Wer hat Anspruch?** Alle Arbeitnehmer (§ 1 Abs. 1, § 22 MiLoG), außer:
- Langzeitarbeitslose in den ersten 6 Monaten (§ 22 Abs. 4 MiLoG)
- Praktikanten bis 3 Monate obligatorisch oder ausbildungsbegleitend (§ 22 Abs. 1 Nr. 2–3 MiLoG)
- Minderjährige ohne abgeschlossene Berufsausbildung (§ 22 Abs. 2 MiLoG)
- Personen in Berufsausbildung (§ 22 Abs. 3 MiLoG – nur BBiG-Mindestvergütung)

**Aufzeichnungspflicht** (§ 17 MiLoG): Beginn, Ende, Dauer der täglichen Arbeitszeit bei Arbeitnehmern nach § 2a SchwarzArbG (geringfügig Beschäftigte, bestimmte Branchen) – täglich aufzeichnen, 2 Jahre aufbewahren.

**Branchenmindestlöhne** (§ 7 AEntG): Abweichend höhere Mindestlöhne in Bau, Elektrohandwerk, Gebäudereinigung, Pflege, Sicherheitsbranche, Fleischwirtschaft u.a.

### 4. EFZG (Entgeltfortzahlungsgesetz)

**Grundregel (§ 3 EFZG):**
- Anspruch auf 6 Wochen Entgeltfortzahlung bei Arbeitsunfähigkeit durch Krankheit
- Voraussetzung: Arbeitsverhältnis besteht seit 4 Wochen (§ 3 Abs. 3 EFZG)
- Für dieselbe Krankheit entsteht neuer Anspruch nach 6-monatiger Pause oder nach 12 Monaten seit letztem Anspruch

**Nachweispflichten:**
- Krank meldung am 1. Krankheitstag (Pflicht aus Arbeitsvertrag oder TV)
- AU-Bescheinigung (gelber Schein / eAU) – Vorlage ab 1. oder 3. Tag (§ 5 EFZG; Arbeitgeber kann 1. Tag verlangen)
- Seit 01.01.2023: elektronische AU-Bescheinigung (eAU) – Arzt übermittelt direkt an Krankenkasse; Arbeitgeber ruft digital ab (§ 5 Abs. 1a EFZG)

**Leistungsverweigerungsrecht (§ 7 EFZG):** Arbeitgeber kann Fortzahlung verweigern, bis AU-Bescheinigung vorgelegt wird.

### 5. Überstunden

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Freizeitausgleich vor Auszahlung bevorzugen, um Lohnnebenkostenbelastung zu reduzieren.
- Überstunden-Dokumentationspflicht (aus BAG-Rspr. seit CCOO-Entscheidung EuGH): `[Modellwissen – prüfen]`.

### 6. Antwortformat

Frage des Nutzers beantworten:
1. Direkte Antwort in einem Satz (ja/nein/es kommt an auf X)
2. Einschlägige Norm mit Zitat
3. Abweichungen durch Tarifvertrag oder Betriebsvereinbarung
4. Grenzfall-Kennzeichnung `[prüfen]` falls nötig

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-buergerliches-recht.md`.

Wesentliche Quellen:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Riechert/Nimmerjahn, MiLoG, 3. Aufl. 2021, § 1 Rn. 1 ff.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Schmitt, EFZG, 9. Aufl. 2023, § 3 Rn. 1 ff.

## Ausgabeformat

Kurze, präzise Antwort:

```
LOHN- UND ARBEITSZEITFRAGE – [Thema] – [Datum]

Frage: [Frage wiederholen]
Jurisdiktion: [Bundesland / Tarifvertrag]

Antwort: [1–3 Sätze, direkt]
Norm: [§ ... ArbZG / MiLoG / EFZG]
Nachweis: [Zitat Rspr. oder Kommentar]

Abweichungen durch TV/BV: [ggf.]
Grenzfall-Flags: [ggf. [prüfen]]
```

## Beispiele

**Frage:** Muss ich Überstunden bezahlen, wenn der Arbeitsvertrag sagt "Überstunden sind mit dem Gehalt abgegolten"?

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Frage:** Wie viele Stunden darf ein Mitarbeiter täglich arbeiten?

**Antwort:** Regulär max. 8 Stunden täglich (§ 3 S. 1 ArbZG), verlängerbar auf max. 10 Stunden, wenn innerhalb von 6 Kalendermonaten oder 24 Wochen im Durchschnitt 8 Stunden nicht überschritten werden (§ 3 S. 2 ArbZG). Durch Tarifvertrag sind weitere Ausnahmen möglich (§ 7 ArbZG), z.B. Bereitschaftsdienst bis 12 h.

## Risiken / typische Fehler

- **Aktualität des Mindestlohnsatzes** - Aktueller Wert: EUR 13,90 ab 01.01.2026 (Fuenfte Mindestlohnanpassungsverordnung); EUR 14,60 ab 01.01.2027 vorgesehen. Vor Ausgabe immer aktuellen Wert in bundesregierung.de / bmas.de pruefen.
- **Tarifbindung ignoriert** - Branchentarifvertraege koennen hoehere Mindestloehne oder abweichende Arbeitszeiten vorsehen.
- **eAU-Umstellung uebersehen** - seit 01.01.2023 laeuft AU-Meldung digital; Arbeitgeber muss dies in HRIS-System abbilden.
- **Arbeitszeiterfassungspflicht** - BAG, Beschluss vom 13.09.2022 - 1 ABR 22/21 (Pflicht zur Arbeitszeiterfassung aus § 3 Abs. 2 Nr. 1 ArbSchG i.V.m. EuGH C-55/18 "CCOO"). Gesetzgeberische Konkretisierung im ArbZG noch ausstehend, Stand vor Ausgabe pruefen. Quelle: dejure.org-Vernetzung BAG 13.09.2022 - 1 ABR 22/21.

## 2. `mandat-triage-arbeitsrecht`

**Fokus:** Eingangs-Abfrage für arbeitsrechtliche Mandate — Mandant fragt nach Kündigung Aufhebungsvertrag Abmahnung Lohn Urlaub Befristung Betriebsuebergang Diskriminierung oder Betriebsrats-Streit. Klaert Mandantenrolle (Arbeitnehmer Arbeitgeber Betriebsrat Geschäftsführer). Sofort-Fristen-Check § 4 KSchG drei Wochen Kündigungsschutzklage § 17 TzBfG drei Wochen Entfristung. Normen § 1 KSchG § 611a BGB § 102 BetrVG § 17 KSchG Massenentlassung. Eskalation Telefon-Sofort bei Kündigung mit drohender Klagefrist Massenentlassung Betriebsuebergang. Output Triage-Memo mit Fristen-Ampel und Routing zu kündigungs-prüfung betriebsrat-anhoerung oder entfristung-Skills. Abgrenzung zu mandat-arbeitsbereich (Workspace-Verwaltung).

### Mandat-Triage Arbeitsrecht

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Arbeitsrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Arbeitsrechtliche Mandate sind fristen-kritisch — die Drei-Wochen-Frist § 4 KSchG ist absolut. Triage stellt richtige Eskalation sicher.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Arbeitnehmer
- Arbeitgeber Mittelstand
- Konzern-Arbeitgeber
- Betriebsrat
- Geschäftsführer (DienstvertragsBereich)
- Aufsichtsrat (Mitbestimmung)
- Tarifvertragspartner
- Schwerbehindertenvertretung

### Frage 2 — Sachgebiet?

- Kündigung (Arbeitgeber- Arbeitnehmer- ordentlich außerordentlich)
- Aufhebungsvertrag / Abwicklungsvereinbarung
- Abmahnung
- Lohn- und Gehalt
- Urlaub Urlaubsabgeltung
- Befristung
- Betriebsübergang
- AGG / Diskriminierung
- Betriebsrats-Streit (§§ 99 102 BetrVG)
- Tarifverhandlung
- Mutterschutz Elternzeit
- Datenschutz im Beschäftigungsverhältnis
- Whistleblowing HinSchG
- Interne Untersuchung
- Compliance
- Statusfeststellung (Scheinselbstständigkeit)
- D&O / Geschäftsführer-Vertrag

### Frage 3 — Akute Eilbedürftigkeit?

- **Drei-Wochen-Frist § 4 KSchG**
- Aufhebungsvertrag bis Datum X zu unterzeichnen
- Anhörung Betriebsrat heute
- Massenentlassung droht
- Interne Untersuchung läuft mit Anhörung morgen
- Whistleblower-Vorwürfe öffentlich
- Streik kurzfristig
- **DSGVO-Auskunftsersuchen nach Art. 15 DSGVO eingegangen oder angekündigt?** → Monatsfrist Art. 12 Abs. 3 DSGVO läuft; unberechtigte Ablehnung löst Art.-82-Schadensersatz aus

### Frage 4 — Stand?

- Beratungsbedarf vor Vertrag
- Vertrag läuft — laufender Streit
- Kündigung erhalten / ausgesprochen
- Aufhebungsvertrag liegt vor
- Schlichtungsstelle / Einigungsstelle
- Klage erhoben (Az ArbG)
- Berufung (LAG)
- Revision (BAG)
- BVerfG / EuGH

### Frage 5 — Vertragsgrundlage?

- Anwendbares Recht (deutsches Recht?)
- Schriftlicher Arbeitsvertrag?
- Tarifvertrag (welcher)?
- Betriebsvereinbarungen?
- Konzern-Betriebsvereinbarungen?
- Richtlinien
- Bonusregelung

### Frage 6 — Frist?

- **§ 4 KSchG** drei Wochen ab Zugang Kündigung
- **§ 7 KSchG** Verstreichen Frist Fiktion Wirksamkeit
- **§ 17 KSchG** Massenentlassung Anzeige
- **§ 102 BetrVG** Betriebsrats-Anhörung eine Woche bei ordentlicher Kündigung
- **§ 626 Abs. 2 BGB** außerordentliche Kündigung zwei Wochen
- **Sperrzeit § 144 SGB III** Aufhebungsvertrag drei Monate
- **Tarifliche Ausschlussfristen** typisch zwei oder drei Monate
- **Lohnverjährung** drei Jahre § 195 BGB

### Frage 7 — Konflikt-Check?

- Andere Anwälte derselben Kanzlei vertreten Gegenseite in selber Sache?
- Bei Arbeitgeber-Vorratsmandant Mitarbeiter-Mandate konfliktäre?
- Konzern-Konstellation

### Frage 8 — Wirtschaftliche Verhältnisse?

- Mandanten-Einkommen für PKH?
- Rechtsschutz-Versicherung mit Wartezeit?
- D&O-Versicherung bei Geschäftsführer
- Berufshaftpflicht Arbeitgeber

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Kündigung | `kuendigungs-pruefung` |
| Kündigungsschutzklage | `kuendigungsschutzklage` |
| Aufhebungsvertrag | `aufhebungsvertrag` |
| Abmahnung | `abmahnung-arbeitsrecht` |
| Betriebsübergang | `betriebsuebergang-613a-pruefen` |
| Lohn-Streit | `lohn-arbeitszeit-fragen` |
| Betriebsrat-Anhörung | `betriebsrat-anhoerung` |
| Statusfeststellung | `arbeitnehmer-status` |
| Lohnsteuer/SV | `lohnsteuer-sozialversicherung` |
| Interne Untersuchung | `interne-untersuchung` |
| Untersuchung Memo | `untersuchungs-memo` |
| AGG Diskriminierung | (Skill agg-diskriminierung — perspektivisch) |
| Befristung | (Skill befristung-tzbfg — perspektivisch) |
| HinSchG Whistleblower | `hinschg-whistleblower-antwort` |
| Massenentlassung | `massenentlassung-17-kschg` |
| Mindestlohn / Zeiterfassung | `mindestlohn-arbeitszeit-erfassung` |
| Aufhebungsvertrag mit Sperrzeit-Risiko | `aufhebungsvertrag-sperrzeit-prognose` |
| AGG Diskriminierung + DSGVO | `agg-pruefung-bewerber-und-beschaeftigte` |

## DSGVO-Auskunftsersuchen — Parallel-Triage

Bei jedem Kündigungs-, Aufhebungsvertrag- oder AGG-Mandat zusätzlich prüfen:

**Liegt zugleich ein DSGVO-Auskunftsersuchen nach Art. 15 DSGVO vor?**

| Indiz | Bewertung |
|---|---|
| Auskunftsersuchen zeitgleich mit Kündigung oder Klage | Typisches Druckmittel; Monatsfrist Art. 12 Abs. 3 DSGVO beachten |
| Standardisierter Legal-Tech-Antrag identischen Wortlauts | Missbrauchsverdacht aus Art. 12 Abs. 5 DSGVO grundsaetzlich denkbar; aktuelle Rechtsprechung jedoch zurueckhaltend bei Annahme von Rechtsmissbrauch |
| Erstmaliger Antrag ohne Legal-Tech-Muster | Hohe Hürde für Missbrauchseinwand; Auskunft erteilen |

**Aktuelle Rechtsprechung zum DSGVO-Schadensersatz bei verspaeteter Auskunft**: BAG, Urteil vom 20.02.2025 - 8 AZR 61/24: Bloss verspaetete Auskunft begruendet keinen Schadensersatzanspruch nach Art. 82 DSGVO; allein ein "Stoergefuehl" oder negative Emotion genuegt nicht. Erforderlich ist konkret begruendete Furcht vor Datenmissbrauch oder tatsaechlicher Kontrollverlust. Quelle: dejure.org-Vernetzung BAG 20.02.2025 - 8 AZR 61/24.

**Handlungsanweisung:**
1. Datum des Eingangs des Auskunftsersuchens dokumentieren.
2. Monatsfrist Art. 12 Abs. 3 DSGVO in Fristenbuch eintragen.
3. Pruefen, ob die Auskunft inhaltlich vollstaendig erteilt werden kann (vgl. BAG 20.02.2025 - 8 AZR 61/24 zur Schadensersatz-Schwelle).
4. Falls Missbrauchseinwand nicht sicher: Auskunft erteilen oder begründet verzögern (max. zwei weitere Monate, Art. 12 Abs. 3 S. 2 DSGVO).
5. Ausgleichsklausel im Aufhebungsvertrag: DSGVO-Ansprüche und Art.-82-Schadensersatz einbeziehen?
6. Zuständigkeit: Auskunftsklage gehört vor das Landgericht (§ 44 BDSG i.V.m. Art. 79 DSGVO), nicht vor das Arbeitsgericht.

Querverweis: `arbeitsrecht/skills/kuendigungs-pruefung/SKILL.md` (Abschnitt DSGVO-Auskunftsersuchen als Druckmittel) und `arbeitsrecht/skills/aufhebungsvertrag/SKILL.md` (DSGVO-Auskunftsersuchen als Verhandlungshebel).

## Mandatsannahme

- **Konflikt-Check** sehr strikt — keine Doppel Mandanten Mandant/Mandant
- **Streitwert** typischer KSchG-Streit drei Monatsgehälter
- **Versicherungs-Deckung** Berufshaftpflicht Arbeitgeber Rechtsschutz Arbeitnehmer
- **Komplexität** Massenentlassung / Konzern-Restrukturierung

## Eskalation

- **Telefon-Sofort** Drei-Wochen-Frist § 4 KSchG läuft binnen Tagen
- **Binnen einer Stunde** Aufhebungsvertrag heute zu unterzeichnen
- **Heute** Klageeinreichung KSchG-Klage Anhörung Betriebsrat
- **Diese Woche** Schriftsatz-Erstentwurf Verteidigungs-Strategie

## Ausgabe

- `triage-protokoll-arbeitsrecht.md`
- Aktenanlage
- Frist im Fristenbuch (§ 4 KSchG Sperrzeit etc.)
- KSchG-Klage-Entwurf bei akutem Bedarf
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

## Quellen

- BGB § 613a § 626
- KSchG §§ 1 4 7 17
- BetrVG §§ 99 102 111 112 113
- TzBfG
- AGG
- HinSchG
- SGB III § 144
- BAG Std.Spruch
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 3. `massenentlassung-17-kschg`

**Fokus:** Prüfungslinie für massenentlassung 17 kschg: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

### Massenentlassung § 17 KSchG

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Massenentlassung § 17 KSchG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Zweck

Bei Massenentlassungen ist § 17 KSchG zwingend zu beachten — sonst sind alle Kündigungen unwirksam. Strenge Vorgaben aus EuGH- und BAG-Rechtsprechung; Heilung nach Ausspruch der Kuendigung ist ausgeschlossen.

## Aktuelle Leitentscheidungen (Stand Mai 2026)

- **BAG, Urteile vom 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22**: Fehler im Anzeigeverfahren (komplett fehlende oder vor Abschluss des Konsultationsverfahrens verfruehte Massenentlassungsanzeige) fuehren zur Unwirksamkeit aller Kuendigungen; eine Heilung nach Kuendigungsausspruch ist ausgeschlossen.
 - Quelle: dejure.org, Vernetzung BAG 01.04.2026 - 6 AZR 152/22; BAG-Pressemitteilung "Massenentlassung - Rechtsfolge von Fehlern im Anzeigeverfahren"; Volltext PDF auf bundesarbeitsgericht.de (Wp-Content) verfuegbar.
- **EuGH, Urteile vom 30.10.2025 - C-134/24 (Tomann) und C-402/24 (Sewel)**: Die Massenentlassungsanzeige nach Art. 4 RL 98/59/EG ist Wirksamkeitsvoraussetzung der Kuendigung; eine fehlende oder verfruehte Anzeige kann nach Kuendigungsausspruch nicht nachgeholt oder geheilt werden. Die 30-Tage-Sperrfrist beginnt erst mit ordnungsgemaesser Anzeige.
 - Quelle: dejure.org, Vernetzung EuGH 30.10.2025 - C-134/24 und C-402/24.

## Schritt 1 — Schwellenwert prüfen

### Betriebsgröße

| Betriebsgröße (Arbeitnehmer) | Schwellenwert für Massenentlassung |
|---|---|
| 21 bis 59 | über fünf |
| 60 bis 499 | mindestens zehn Prozent oder mehr als fünfundzwanzig |
| Ab 500 | mindestens dreißig |

### Zeitraum

- **Dreißig Kalendertage** Berechnungs-Zeitraum
- Vor und nach jeweiliger Kündigung zu zählen
- Bei Aufhebungs-Vereinbarungen mit Kündigungs-Anstoß durch Arbeitgeber: zählend

### Begriff Arbeitnehmer

- **Alle Beschäftigten** Voll- Teil- Leiharbeiter eingerechnet
- **Geschäftsführer** nicht
- **Leitende Angestellte** auf Mitarbeiter-Ebene ja

### Begriff Entlassung

- **Arbeitgeberseitige Kündigung** zählt
- **Aufhebungsvertrag** auf Arbeitgeber-Initiative zählt
- **Befristungs-Ablauf** zählt nicht
- **Eigen-Kündigung** Arbeitnehmer zählt nicht

## Schritt 2 — Konsultations-Pflicht Betriebsrat § 17 Abs. 2 KSchG

### Zeitpunkt

- **Vor Massenentlassungs-Anzeige**
- **Vor Zugang der Kündigungen**

### Inhalt

Schriftlich an Betriebsrat:

- Gründe der Massenentlassung
- Zahl und Berufsgruppe zu Entlassender
- Zahl und Berufsgruppe der gewöhnlich Beschäftigten
- Zeitraum
- Auswahl-Kriterien
- Berechnung von Abfindungen
- Anschriften der Agentur für Arbeit

### Frist

- **Zwei Wochen** Konsultations-Zeit
- BR kann Stellungnahme abgeben — Pflicht des AG zu Beraten

### Folge der Konsultation

- **Erfolgreich beraten** — Bescheinigung BR oder Pflicht-Hinweis "BR hat sich nicht geäußert"
- **Nichtbeteiligung BR** — Kündigung unwirksam

## Schritt 3 — Massenentlassungs-Anzeige § 17 Abs. 1 KSchG

### Adressat

- **Agentur für Arbeit** des Betriebs-Sitzes
- **Schriftform** Original
- **Vor Zugang Kündigung**

### Inhalt (§ 17 Abs. 3 KSchG)

- Name Anschrift Arbeitgeber
- Zahl Berufsgruppen Gesamt-Beschäftigung
- Zahl Berufsgruppen zu Entlassender
- Zeitraum
- Auswahl-Kriterien
- Abfindungs-Berechnung
- Stellungnahme oder Information über BR-Konsultation

### Bestätigung Eingang

- Agentur für Arbeit bestätigt Eingang
- **Sperrfrist** ein Monat ab Anzeige § 18 KSchG
- Vorzeitige Beendigung möglich auf Antrag

### Folge bei Mangel der Anzeige

- BAG, Urteile vom 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22, sowie EuGH, Urteile vom 30.10.2025 - C-134/24 und C-402/24: Fehlende oder verfruehte (vor Abschluss der BR-Konsultation eingereichte) Massenentlassungsanzeige fuehrt zur Unwirksamkeit aller davon erfassten Kuendigungen. Eine Heilung nach Kuendigungsausspruch ist ausgeschlossen. Quellen: dejure.org-Vernetzungen; BAG-Pressemitteilung "Massenentlassung - Rechtsfolge von Fehlern im Anzeigeverfahren".
- Nicht jeder Verfahrensfehler fuehrt zur Unwirksamkeit; insbesondere die bloss unterbliebene Uebermittlung der Abschrift nach § 17 Abs. 3 Satz 1 KSchG ist nach BAG 6 AZR 155/21 für sich allein kein zur Unwirksamkeit fuehrender Fehler.

## Schritt 4 — Reihenfolge der Schritte

1. **Plan** Massenentlassung intern
2. **Beratung mit Betriebsrat** zwei Wochen ab Info-Übergabe
3. **Sozialplan / Interessensausgleich** § 111 BetrVG
4. **Anzeige Agentur für Arbeit** vor Kündigungen
5. **Eingangsbestätigung abwarten**
6. **Sperrfrist berücksichtigen** ein Monat
7. **Kündigungen aussprechen** unter Beachtung KSchG Schutzbestimmungen

## Schritt 5 — Sozialplan und Interessensausgleich § 111 BetrVG

### Betriebsänderung

- Massenentlassung über Schwellenwert
- Stilllegung Betriebsteil
- Verlegung Betriebsstandort

### Interessensausgleich

- Verhandlungs-Verfahren mit BR
- Schiedsstelle bei Nicht-Einigung
- Inhalt: Wie wird Betriebsänderung durchgeführt

### Sozialplan

- **Erzwingbar** durch Einigungsstelle § 112 Abs. 4 BetrVG
- Inhalt: Abfindungen Umschulungs-Hilfen Wegfall-Ausgleich

### Nachteilsausgleich § 113 BetrVG

- Bei Massenentlassung ohne Interessensausgleich
- Anspruch des einzelnen Arbeitnehmers

## Schritt 6 — Sozialauswahl § 1 Abs. 3 KSchG

### Soziale Kriterien

- Lebensalter
- Beschäftigungs-Dauer
- Unterhalts-Verpflichtungen
- Schwerbehinderung

### Gewichtung

- Punkteschema möglich
- Auswahlrichtlinie mit Betriebsrat § 95 BetrVG
- Spielraum begrenzt

### Berechtigte Interessen Arbeitgeber

- Berufliche Qualifikation
- Leistung
- Bestimmte Auftragslage

## Schritt 7 — Kündigungsschutz-Sonderfälle

### Schwerbehinderte § 168 SGB IX

- Zustimmung Integrationsamt

### Schwangere § 17 MuSchG

- Zustimmung obere Landesbehörde

### Elternzeit § 18 BEEG

- Zustimmung obere Landesbehörde

### Betriebsratsmitglieder § 15 KSchG

- Außerordentlich nur — Zustimmung BR

## Schritt 8 — Kündigungsschutzklage parallel

- **Drei-Wochen-Frist** § 4 KSchG individuell beachten
- Bei Mängeln § 17 KSchG ohnehin Klage erfolgsversprechend
- Skill `kuendigungsschutzklage`

## Schritt 9 — Strategische Aspekte

### Bei Eilbedürftigkeit

- Konsultationsfrist zwei Wochen Mindest-Dauer
- Anzeigesperrfrist ein Monat
- Gesamt-Lauf mindestens sechs Wochen
- Eilkündigungen praktisch nicht möglich

### Bei Massenentlassung in Insolvenz

- § 125 InsO Sonder-Regelungen
- Erleichterte Kündigungsfrist
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Schritt 10 — Beweissicherung

- **Konsultations-Schreiben BR** mit Empfangs-Bestätigung
- **BR-Stellungnahme** in Akte
- **Anzeige-Schreiben AfA** mit Eingangs-Bestätigung
- **Zeitlinie** dokumentiert

## Checkliste

- Schwellenwert erfüllt?
- Welche Personen sind Arbeitnehmer i.S.d. KSchG?
- BR konsultiert? Datum?
- Stellungnahme BR vorhanden / abgewartet?
- AfA-Anzeige eingereicht? Datum? Vollständig?
- Sperrfrist ein Monat berücksichtigt?
- Sozialauswahl durchgeführt?
- Schutz-Berechtigte separat?
- Sozialplan-Verhandlungen?

## Ausgabe

- `massenentlassung-{az}.md`
- BR-Konsultations-Schreiben Vorlage
- Anzeige-Schreiben AfA Vorlage
- Sozialauswahl-Tabelle
- Frist-Plan
- Bei Verstoß: Verteidigungs-Strategie Arbeitnehmer

## Quellen

- KSchG §§ 1 4 17 18
- BetrVG §§ 95 111 112 113
- SGB IX § 168
- MuSchG § 17
- BEEG § 18
- Richtlinie 98/59/EG (Massenentlassungs-Richtlinie), insbesondere Art. 2 (Konsultation) und Art. 4 (Anzeige; 30-Tage-Sperrfrist)
- BAG, Urteile vom 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22 (Unwirksamkeit bei Fehlern im Anzeigeverfahren) - dejure.org / bundesarbeitsgericht.de
- EuGH, Urteile vom 30.10.2025 - C-134/24 und C-402/24 (keine Heilung fehlender oder verfruehter Anzeige) - dejure.org
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## 4. `mindestlohn-arbeitszeit-erfassung`

**Fokus:** Prüfungslinie für mindestlohn arbeitszeit erfassung: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

### Mindestlohn und Arbeitszeit-Erfassung

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mindestlohn und Arbeitszeit-Erfassung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre vor jeder Bearbeitung

1. Handelt es sich um eine Klage des Arbeitnehmers (Lohnnachzahlung) oder um eine Compliance-Prüfung des Arbeitgebers?
2. Besteht ein Zeiterfassungssystem? Falls ja: welche Art (elektronisch, Stundenzettel, Vertrauensarbeitszeit)?
3. Welche Branche? (Branchen-Mindestlohn möglicherweise höher als allgemeiner MiLoG-Satz)
4. Liegt ein Tarifvertrag vor? (Tariflicher Lohn geht vor, MiLoG ist Untergrenze)
5. Klageziel: Lohnnachzahlung, OWi-Abwehr, System-Einführung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Anspruchsgrundlagen & Normen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- § 1 MiLoG — Mindestlohnanspruch
- § 17 MiLoG — Dokumentationspflicht (Aufbewahrung sechs Jahre)
- § 21 MiLoG — Bußgeld bis 500.000 EUR
- § 23 MiLoG — Ausschluss öffentliche Vergabe
- Art. 31 Abs. 2 GRC; RL 2003/88/EG (Arbeitszeitrichtlinie)
- § 26 BDSG / Art. 6 Abs. 1 lit. b, c DSGVO — Beschäftigtendatenschutz
- § 87 Abs. 1 Nr. 6 BetrVG — Mitbestimmung bei Einführung des Erfassungssystems

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt 1 — Rechtliche Grundlage Arbeitszeit-Erfassung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **14.5.2019**
- **Mitgliedstaaten müssen** Arbeitgeber zur Einrichtung eines objektiven verlässlichen zugänglichen Systems zur Erfassung der gesamten Arbeitszeit verpflichten
- Begründung: Effektivität der Arbeitszeit-Richtlinie 2003/88/EG (Höchst-Arbeitszeit Ruhezeiten)

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- **Auslegung § 3 Abs. 2 Nr. 1 ArbSchG**
- Bereits geltendes Recht: Arbeitgeber **muss** Arbeitszeit erfassen
- Nicht nur Überstunden — **gesamte** Arbeitszeit
- Beginn Ende Pausen
- Pflicht greift unabhängig davon ob Arbeitnehmer-Recht eingefordert

### Anforderungen

- **Objektiv** — nicht nur Selbstangabe
- **Verlässlich** — manipulationssicher
- **Zugänglich** — Arbeitnehmer kann Aufzeichnungen einsehen

### Erfassungs-Methoden

- Elektronische Zeit-Erfassungs-Systeme (RFID-Karte Zeiterfassungs-Software)
- Schriftliche Stundenzettel mit Unterschrift
- Apps mit GPS / Geo-Fencing
- Vertrauens-Arbeitszeit problematisch — bedarf System-Bestätigung

## Schritt 2 — Konsequenz bei Verstoß

### Beweis-Erleichterung Mindestlohn-Klage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Bei fehlender Erfassung** Arbeitnehmer-Vortrag ausreichend wenn substantiiert
- **Arbeitgeber muss** Gegen-Vortrag bringen
- Praktisch: Beweis-Umkehrungs-ähnliche Wirkung

### Mindestlohn-Vorwurf

- Bei fehlendem System leicht zu Mindestlohn-Vorwurf
- Arbeitgeber kann Stunden nicht widerlegen
- Klage kann erfolgreich sein

### OWi-Risiko

- § 21 MiLoG bis EUR 500.000
- § 23 MiLoG Ausschluss öffentliche Vergabe bis drei Jahre

## Schritt 3 — Mindestlohn-Höhe

### Allgemeiner Mindestlohn

| Datum | Stunden-Satz | Rechtsgrundlage |
|---|---|---|
| 1.1.2024 | EUR 12,41 | Vierte Mindestlohnanpassungsverordnung |
| 1.1.2025 | EUR 12,82 | Vierte Mindestlohnanpassungsverordnung |
| 1.1.2026 | EUR 13,90 | Fuenfte Mindestlohnanpassungsverordnung vom 05.11.2025 (BGBl. 2025 I Nr. 268) |
| 1.1.2027 | EUR 14,60 | Fuenfte Mindestlohnanpassungsverordnung vom 05.11.2025 (BGBl. 2025 I Nr. 268) |
| Kuenftig | Empfehlung der Mindestlohn-Kommission, Umsetzung durch Verordnung BMAS | § 11 MiLoG |

Quelle: bundesregierung.de / bmas.de (Pressemitteilung "Mindestlohn steigt zum 1. Januar 2026 auf 13,90 Euro"). Die Minijob-Verdienstgrenze passt sich an: 2026 = 603 EUR (Deutsche Rentenversicherung Baden-Wuerttemberg, Pressemitteilung 22.12.2025).

### Branchen-Mindestlöhne (Auswahl)

- **Bau** TV-Mindestlohn typisch über allgemein
- **Pflege** TV-Mindestlohn
- **Gebäudereinigung** TV-Mindestlohn
- **Leiharbeit** TV-Mindestlohn

### Berechnung

```
Mindestlohn-Anspruch = Stunden x Stundensatz

Beispiel:
40 Wochenstunden x 4.33 Wochen x EUR 12,82 = EUR 2.222 Monatsmindestlohn
```

## Schritt 4 — Arbeitszeit-Begriff

### Was zählt zur Arbeitszeit

- **Tätigkeits-Zeit** am Arbeitsplatz
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Pausen** wenn Mandant arbeitsbereit (echte Pause nicht)

### Was nicht zählt

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Echte Pausen** ohne Arbeitsbereitschaft

### Bereitschaftsdienst vs. Rufbereitschaft

- **Bereitschaftsdienst** anwesend am Arbeitsplatz — Arbeitszeit
- **Rufbereitschaft** zu Hause / Aufenthaltsort frei — keine Arbeitszeit (im Standard)
- Bei sehr enger Reaktions-Zeit-Anforderung Übergang zu Bereitschaftsdienst (EuGH-Linie)

## Schritt 5 — Praktische Klage-Konstellation Arbeitnehmer

### Vorprüfung

- **Tatsächliche Arbeitsstunden** rekonstruieren (eigene Aufzeichnungen E-Mail-Logs Login-Logs)
- **Bezahlte Stunden** aus Lohn-Abrechnungen
- **Differenz** = Mindestlohn-Vorwurf

### Klage-Vorbereitung

- **Substantiierter Vortrag** mit Stunden-Aufstellung
- **Arbeitgeber-System fehlt** Argumentation
- **Beweisangebote**: Zeugen, Kollegen-Aussagen, eigene Aufzeichnungen, Login-Logs

### Schadensersatz / Lohn-Forderung

- **Lohnnachzahlung** in Höhe der Differenz
- **Verzugs-Zinsen** § 288 BGB 5 Prozentpunkte über Basiszinssatz
- **Anwaltskosten** vorgerichtlich als Verzugsschaden

### Verjährungs-Frist

- **Drei Jahre** §§ 195, 199 BGB ab Schluss des Jahres der Fälligkeit
- Bei Tarif-Ausschluss-Frist möglicherweise kürzer (Tarif-Prüfung)

## Schritt 6 — Verteidigung Arbeitgeber

### Erste Antwort

- Aufzeichnungen aus Zeit-Erfassungs-System vorlegen
- Wenn System fehlt → Schadenslimitierung

### Argumentations-Linien

- **Vertrauens-Arbeitszeit** mit dokumentiertem Verfahren
- **Stunden-Begrenzung** durch Vertrag (bei kollektiv-rechtlicher Pflicht)
- **Pausen-Zeit** dokumentiert
- **Rufbereitschaft vs. Bereitschaftsdienst** Unterscheidung

### Schadenslimitation

- Bei substantiierter Mandanten-Klage Vergleichs-Verhandlung
- Branchen-Üblichkeit als Argument
- Streit-Reduktion

### Sofortmaßnahmen

- **Zeit-Erfassungs-System einführen** sofort
- **Schulung** Vorgesetzte
- **Auditierung** alte Stunden
- **Compliance-Dokumentation**

## Entscheidungsbaum Arbeitgeber-Compliance

```
Besteht ein Zeiterfassungssystem?
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (objektiv, verlässlich, zugänglich, gesamte Arbeitszeit)
 Ja → Aufbewahrung 6 Jahre § 17 MiLoG gewährleistet?
 Ja → OK
 Nein → Aufbewahrungspflicht nachrüsten
 Nein → System nachrüsten; BR-Mitbestimmung § 87 Abs. 1 Nr. 6 BetrVG!
 Nein → System einführen (sofort)
 Betrieb mit BR? → Betriebsvereinbarung abschließen
 Kein BR? → Weisung AG
 Datenschutzbeauftragten einbinden
```

## Schritt 7 — Konkretes Erfassungs-System

### Anforderungen

- Elektronisch oder schriftlich
- **Tägliche Erfassung** Beginn Ende Pausen
- **Manipulations-Sicherheit** Logs Audit-Trail
- **Zugänglichkeit** für Arbeitnehmer (Einsicht eigene Stunden)
- **Aufbewahrungs-Frist** zwei Jahre § 16 ArbZG, sechs Jahre § 17 MiLoG, zehn Jahre § 147 AO

### Datenschutz-Aspekte

- DSGVO Art. 6 Abs. 1 lit. b (Vertrags-Erfüllung) + lit. c (gesetzliche Verpflichtung)
- § 26 BDSG Beschäftigten-Datenschutz
- Betriebsrat-Mitbestimmungs-Recht § 87 Abs. 1 Nr. 6 BetrVG (Überwachung Verhalten Leistung)
- Tracking-Funktionen begrenzt einsetzen

### Mitbestimmungs-Recht Betriebsrat

- Bei Einführung System Pflicht-Vereinbarung
- Bei Verweigerung Einigungsstelle § 76 BetrVG

## Schritt 8 — Spezielle Konstellationen

### Home-Office / Remote-Arbeit

- Erfassungs-Pflicht gilt
- Login-Logs Webcam-Bilder problematisch (Verhältnismäßigkeit)
- Selbst-Aufzeichnung mit Vertrauens-Bestätigungs-Mechanismus

### Vertrauens-Arbeitszeit

- Modell zulässig wenn System der Erfassung trotzdem existiert
- Mitarbeiter erfasst selbst — Arbeitgeber sichert System

### Außendienst

- App-basierte Erfassung
- GPS-Daten datenschutzrechtlich sensitiv
- Datenschutz-Beauftragten einbinden

### Führungs-Personal

- **Leitende Angestellte** § 5 BetrVG eingeschränkte Anwendung
- **Geschäftsführer** keine Arbeitnehmer
- **Außerordentlich Befreiung** möglich

### Schicht-Modell

- Verschiebungs-Pläne dokumentieren
- Mehrarbeits-Stunden zählen

## Schritt 9 — Lieferketten-Bezug LkSG

### LkSG § 2 Abs. 2 Nr. 8 Mindestlohn

- Mindestlohn-Verstoß bei Lieferanten = LkSG-Risiko
- Bei Mandant als Auftraggeber Sorgfaltspflicht

## Schritt 10 — Bußgeld-Risiken § 21 MiLoG

- **EUR 500.000** bei vorsätzlicher Unterschreitung
- **EUR 30.000** bei fahrlässiger Pflicht-Verletzung
- **EUR 30.000** bei Verstoß gegen Aufzeichnungs-Pflicht § 17 MiLoG

### Ausschluss öffentliche Vergabe § 23 MiLoG

- Bei rechtskräftigem Bußgeld
- Drei Jahre

## Schritt 11 — Tarif-Bezug

### Tariflicher Lohn höher als MiLoG

- Tarifvertrag gilt
- Aber MiLoG als Untergrenze

### Tariflicher Lohn unter MiLoG

- MiLoG hat Vorrang § 1 Abs. 3 MiLoG

### Allgemein-Verbindliche Tarifverträge

- AVE-Erklärung BMAS
- Branchen-Bindung auch Nicht-Tarif-Mitglieder

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Unterlaufen des Mindestlohns aufdecken | Differenzlohanspruch berechnen und geltend machen; Template unten |
| Variante A — laufendes Arbeitsverhaeltnis | Zunaechst ausserbetriebliche Geltendmachung; Kuendigungsschutz beachten |
| Variante B — beendetes Arbeitsverhaeltnis | Direkter Klageweg; Verjährung pruefen (3 Jahre § 195 BGB) |
| Variante C — systematische Verletzung (mehrere AN) | Sammelklage-Vorbereitung; Zoll einschalten erwaegen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template: Klageantrag Mindestlohn

**Adressat:** ArbG [ORT] — Tonfall sachlich-juristisch

```
An das Arbeitsgericht [ORT]

Klage

der/des [NAME], [ADRESSE]
- Klaeger/in -
Prozessbevollmaechtigte: [KANZLEI]

gegen

[FIRMA], [ADRESSE]
- Beklagte -

wegen Mindestlohnzahlung

Antraege:

1. Die Beklagte wird verurteilt, an die Klaeger/in
 EUR [Differenz Mindestlohn / tatsaechlich gezahlt]
 nebst Zinsen in Hoehe von 5 Prozentpunkten ueber
 dem Basiszinssatz seit [Datum] zu zahlen.

Begruendung:

Die Klaeger/in war bei der Beklagten im Zeitraum
[von] bis [bis] beschaeftigt. Die Beklagte hat für
diesen Zeitraum das Mindestlohnversprechen verletzt.

Die Beklagte fuehrte kein objektives verlaessliches
zugaengliches Arbeitszeit-Erfassungs-System
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Die Klaeger/in hat ihre Stunden dokumentiert
(Anlage K1).

[Stunden-Aufstellung mit tagesgenauer Zeit]

Aus den nicht-bezahlten Stunden ergibt sich eine
Forderung von EUR [Betrag] (berechnet nach dem
jeweils geltenden gesetzlichen Mindestlohn:
EUR 12,41 ab 1.1.2024, EUR 12,82 ab 1.1.2025,
EUR 13,90 ab 1.1.2026).
```

## Output-Template: Mandantenschreiben Arbeitgeber-Compliance

**Adressat:** Mandant/HR — Tonfall verständlich-erklärend

```
Sehr geehrte Damen und Herren,

nach unserer Pruefung Ihres Zeiterfassungssystems
ergibt sich folgendes:

1. Handlungsbedarf: [ja/nein — kurze Begruendung]
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Empfohlene Massnahmen mit Zeitplan: [...]
4. Bussgeldrisiko bei Untaetigkeit: bis EUR 500.000

Wir empfehlen folgende Sofortmassnahmen:
[...]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Verzahnung mit anderen Skills

- `kuendigungsschutzklage` — Parallel-Konstellation
- `lohnsteuer-sozialversicherung` — Steuer-Aspekte Nachzahlung
- `betriebsrat-anhoerung` — Mitbestimmungs-Recht
- `interne-untersuchung` — bei systematischen Verstößen

## Ausgabe

- `mindestlohn-{az}.md` mit Stunden-Aufstellung Beweis-Konstellation
- Klage-Schriftsatz / Verteidigungs-Schriftsatz
- Bei Arbeitgeber: System-Einführungs-Empfehlung
- Bußgeld-Risiko-Memo
- Frist im Fristenbuch (Verjährung drei Jahre Tarif-Ausschluss-Frist beachten)

## Quellen

- ArbZG §§ 3 16
- ArbSchG § 3
- MiLoG §§ 1 17 21 23
- BetrVG § 87
- BDSG § 26
- DSGVO Art. 6
- AO § 147
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:
