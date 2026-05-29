---
name: lohn-arbeitszeit-fragen
description: "Standortbezogene Lohn- und Arbeitszeitfragen – ArbZG (Höchstarbeitszeit, Pausen, Ruhezeiten, Aufzeichnungspflichten), MiLoG (Mindestlohn, Aufzeichnungspflicht), EFZG (Entgeltfortzahlung im Krankheitsfall), Tarifverträge, Überstunden. Antwort mit der maßgeblichen Norm und Zitat."
---

# /arbeitsrecht:lohn-arbeitszeit-fragen

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
