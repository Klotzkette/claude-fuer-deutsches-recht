---
name: lohn-arbeitszeit-fragen
description: "Standortbezogene Lohn- und Arbeitszeitfragen – ArbZG (Höchstarbeitszeit, Pausen, Ruhezeiten, Aufzeichnungspflichten), MiLoG (Mindestlohn, Aufzeichnungspflicht), EFZG (Entgeltfortzahlung im Krankheitsfall), Tarifverträge, Überstunden. Antwort mit der maßgeblichen Norm und Zitat."
---

# /arbeitsrecht:lohn-arbeitszeit-fragen

## Zweck

„Es kommt darauf an" ist wahr, aber keine nützliche Antwort. Dieser Skill liefert standortspezifische Antworten mit der maßgeblichen Norm, zitiert und mit Kennzeichnung von Grenzfällen.

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
EuGH, Urt. v. 14.05.2019 – C-55/18 (CCOO), NZA 2019, 683: Mitgliedstaaten müssen objektives, verlässliches und zugängliches System zur Erfassung der täglichen Arbeitszeit einführen. BAG, Beschl. v. 13.09.2022 – 1 ABR 22/21, NZA 2022, 1562: Arbeitgeber ist bereits nach § 3 Abs. 2 Nr. 1 ArbSchG verpflichtet, ein System zur Arbeitszeiterfassung einzuführen `[Modellwissen – prüfen]`. Gesetzliche Ausgestaltung (ArbZG-Reform) noch offen – auf aktuellen Stand prüfen.

### 3. MiLoG (Mindestlohngesetz)

**Aktueller Mindestlohn:** § 1 Abs. 2 MiLoG; zum Stand [aktuelles Datum prüfen]. Anpassung durch Mindestlohnkommission gem. § 9 MiLoG alle 2 Jahre. `[Modellwissen – prüfen, aktuellen Satz abfragen]`

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

- Gesetzlich: keine Pflicht zur Überstundenvergütung, wenn Arbeitsvertrag oder Tarifvertrag Überstunden als „mit dem Gehalt abgegolten" regelt. AGB-Kontrolle beachten: zu weitgehende Klauseln (ohne Stundenbegrenzung) sind unwirksam; BAG, Urt. v. 22.02.2012 – 5 AZR 765/10, NZA 2012, 861 `[Modellwissen – prüfen]`.
- Freizeitausgleich vor Auszahlung bevorzugen, um Lohnnebenkostenbelastung zu reduzieren.
- Überstunden-Dokumentationspflicht (aus BAG-Rspr. seit CCOO-Entscheidung EuGH): `[Modellwissen – prüfen]`.

### 6. Antwortformat

Frage des Nutzers beantworten:
1. Direkte Antwort in einem Satz (ja/nein/es kommt an auf X)
2. Einschlägige Norm mit Zitat
3. Abweichungen durch Tarifvertrag oder Betriebsvereinbarung
4. Grenzfall-Kennzeichnung `[prüfen]` falls nötig

## Quellen und Zitierweise

Zitierstandard: `../references/zitierweise.md`. Methodik: `../references/methodik-deutsches-recht.md`.

Wesentliche Quellen:
- Baeck/Deutsch/Winzer, in: ErfK, 24. Aufl. 2024, ArbZG § 3 Rn. 1 ff.
- Riechert/Nimmerjahn, MiLoG, 3. Aufl. 2021, § 1 Rn. 1 ff.
- EuGH, Urt. v. 14.05.2019 – C-55/18 (CCOO), NZA 2019, 683 (Arbeitszeiterfassung)
- BAG, Beschl. v. 13.09.2022 – 1 ABR 22/21, NZA 2022, 1562 (Pflicht zur Zeiterfassung)
- BAG, Urt. v. 22.02.2012 – 5 AZR 765/10, NZA 2012, 861 (Überstundenpauschalabgeltung)
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

**Frage:** Muss ich Überstunden bezahlen, wenn der Arbeitsvertrag sagt „Überstunden sind mit dem Gehalt abgegolten"?

**Antwort:** Eine solche Klausel ist nur wirksam, wenn die Anzahl der abgegoltenen Überstunden klar begrenzt ist und der Stundensatz über dem Mindestlohn bleibt. Unbegrenzte Pauschalabgeltungsklauseln sind nach § 307 Abs. 1 BGB unwirksam (BAG, Urt. v. 22.02.2012 – 5 AZR 765/10, NZA 2012, 861 `[Modellwissen – prüfen]`). Im Zweifel: Einzelfallprüfung.

**Frage:** Wie viele Stunden darf ein Mitarbeiter täglich arbeiten?

**Antwort:** Regulär max. 8 Stunden täglich (§ 3 S. 1 ArbZG), verlängerbar auf max. 10 Stunden, wenn innerhalb von 6 Kalendermonaten oder 24 Wochen im Durchschnitt 8 Stunden nicht überschritten werden (§ 3 S. 2 ArbZG). Durch Tarifvertrag sind weitere Ausnahmen möglich (§ 7 ArbZG), z.B. Bereitschaftsdienst bis 12 h.

## Risiken / typische Fehler

- **Aktualität des Mindestlohnsatzes** – Anpassungen alle 2 Jahre; vor Ausgabe immer aktuellen Satz prüfen `[Modellwissen – prüfen]`.
- **Tarifbindung ignoriert** – Branchentarifverträge können höhere Mindestlöhne oder abweichende Arbeitszeiten vorsehen.
- **eAU-Umstellung übersehen** – seit 01.01.2023 läuft AU-Meldung digital; Arbeitgeber muss dies in HRIS-System abbilden.
- **Arbeitszeiterfassungspflicht noch im Wandel** – gesetzgeberischer Handlungsbedarf nach BAG-Beschluss v. 13.09.2022; Stand immer prüfen.
