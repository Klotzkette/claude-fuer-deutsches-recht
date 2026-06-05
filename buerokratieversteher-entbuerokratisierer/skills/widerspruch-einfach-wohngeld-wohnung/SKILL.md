---
name: widerspruch-einfach-wohngeld-wohnung
description: "Widerspruch Einfach Wohngeld Wohnung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Widerspruch Einfach Wohngeld Wohnung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Widerspruch Einfach Wohngeld Wohnung** im Plugin Buerokratieversteher Entbuerokratisierer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `widerspruch-einfach` | Erstellt fristwahrenden Widerspruch gegen Verwaltungsakte, wenn Widerspruch statthaft ist, mit knapper Begründung oder Begründungsnachreichung. |
| `wohngeld` | Hilft bei Wohngeldantrag, Mietstufe, Einkommen, Haushaltsmitglieder, Ablehnung, Nachzahlung und Widerspruch. |
| `wohnung-und-obdachlosigkeit` | Routet Wohnungsnotfall, Ordnungsamt, Sozialamt, Kündigung, Räumung und Eilrechtsschutz. |
| `zahlung-stundung-raten` | Formuliert Stundungs-, Ratenzahlungs-, Erlass- oder Aussetzungsantrag bei Forderungen öffentlicher Stellen. |

## Arbeitsweg

Im Plugin Buerokratieversteher Entbuerokratisierer gilt für **Widerspruch Einfach Wohngeld Wohnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `widerspruch-einfach`

**Fokus:** Erstellt fristwahrenden Widerspruch gegen Verwaltungsakte, wenn Widerspruch statthaft ist, mit knapper Begründung oder Begründungsnachreichung.

# Widerspruch einfach

## Aufgabe
Erstellt fristwahrenden Widerspruch gegen Verwaltungsakte, wenn Widerspruch statthaft ist, mit knapper Begründung oder Begründungsnachreichung.

## Normfokus und Praxis
- Anspruchsgrundlage: § 68 ff. VwGO (allgemeines Verwaltungsrecht), § 84 SGG (Sozialrecht), § 348 AO (Steuerrecht). Frist regelmäßig ein Monat (§ 70 VwGO, § 84 SGG, § 355 AO) ab Bekanntgabe.
- Statthaftigkeit: Nicht überall ist Widerspruch eröffnet — in einigen Bundesländern abgeschafft (z. B. NRW teilweise), dann direkt Anfechtungs- oder Verpflichtungsklage. Rechtsbehelfsbelehrung prüfen, bei Fehlen oder Falschbelehrung Jahresfrist nach § 58 Abs. 2 VwGO.
- Form: schriftlich oder zur Niederschrift (§ 70 VwGO). E-Mail nur, wenn Behörde Zugang eröffnet hat (§ 3a VwVfG). Sicher: Einwurf-Einschreiben oder Eingangsbestätigung der Behörde.
- Aufschiebende Wirkung nach § 80 Abs. 1 VwGO Regel, Ausnahmen § 80 Abs. 2 (Abgaben, Polizei-/Ordnungsverfügungen mit Sofortvollzug, ausdrückliche Anordnung). Bei Sofortvollzug Antrag § 80 Abs. 5 VwGO ans Verwaltungsgericht.
- Praktiker-Tipp: Erst nur fristwahrend einlegen ("Widerspruch wird eingelegt; Begründung folgt") — Begründung nach Akteneinsicht (§ 29 VwVfG). Mehrere Adressaten? Pro Bescheid separat.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

## 2. `wohngeld`

**Fokus:** Hilft bei Wohngeldantrag, Mietstufe, Einkommen, Haushaltsmitglieder, Ablehnung, Nachzahlung und Widerspruch.

# Wohngeld

## Aufgabe
Hilft bei Wohngeldantrag, Mietstufe, Einkommen, Haushaltsmitglieder, Ablehnung, Nachzahlung und Widerspruch.

## Normfokus und Praxis
- Rechtsgrundlage: WoGG (Wohngeldgesetz; Wohngeld-Plus seit 1.1.2023 mit Klima- und Heizkostenkomponente), WoGV (Wohngeldverordnung), Mietstufen-VO. Wohngeld als Mietzuschuss (für Mieter) oder Lastenzuschuss (für Eigentümer).
- Anspruchsvoraussetzungen: Mietstufe der Gemeinde (I-VII), Anzahl Haushaltsmitglieder, Gesamteinkommen (§ 13 WoGG, regelmäßig anrechenbar nach §§ 14-21 WoGG), zuschussfähige Miete bzw. Belastung (§§ 9-12 WoGG). Heizkostenkomponente § 12 Abs. 6 WoGG (1.20 EUR pro qm der berücksichtigungsfähigen Wohnfläche).
- Vorrang/Nachrang: Vorrang vor Bürgergeld/Sozialhilfe — Wohngeld auch bei niedrigem Einkommen oft erste Option; nicht kombinierbar mit Bürgergeld nach SGB II für KdU (§ 7 Abs. 1 WoGG).
- Antrag: schriftlich oder elektronisch bei kommunaler Wohngeldbehörde; rückwirkende Bewilligung nicht möglich, nur ab Antragsmonat (§ 25 WoGG); Bewilligungszeitraum regelmäßig 12 Monate.
- Praktiker-Tipp: bei Ablehnung Widerspruch innerhalb eines Monats (§ 70 VwGO); Online-Wohngeldrechner für plausible Anspruchshöhe nutzen; bei Bürgergeld-Antragsteller Wohngeldprüfung gleichzeitig (Vorrangprinzip § 12a SGB II). Erhöhungsanträge bei Mietsteigerung sofort stellen.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

## 3. `wohnung-und-obdachlosigkeit`

**Fokus:** Routet Wohnungsnotfall, Ordnungsamt, Sozialamt, Kündigung, Räumung und Eilrechtsschutz.

# Wohnung und Obdachlosigkeit

## Aufgabe
Routet Wohnungsnotfall, Ordnungsamt, Sozialamt, Kündigung, Räumung und Eilrechtsschutz.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.

## 4. `zahlung-stundung-raten`

**Fokus:** Formuliert Stundungs-, Ratenzahlungs-, Erlass- oder Aussetzungsantrag bei Forderungen öffentlicher Stellen.

# Zahlung, Stundung, Raten

## Aufgabe
Formuliert Stundungs-, Ratenzahlungs-, Erlass- oder Aussetzungsantrag bei Forderungen öffentlicher Stellen.

## Einstieg
Wenn ein Dokument vorliegt, lies zuerst das Dokument. Frage höchstens vier Punkte nach:

1. Welche Rolle hat die betroffene Person oder Organisation?
2. Welche Frist, welcher Termin oder welche Sanktion steht im Raum?
3. Welche Behörde, welches Gericht, welches Register, welcher Verband oder welche Wahlstelle handelt?
4. In welcher Sprache und Detailtiefe soll erklärt oder formuliert werden?

## Arbeitsworkflow
1. **Prüfschritt:** Dokument oder Anliegen zuerst in einfache, sichere Einzelschritte zerlegen.
2. **Prüfschritt:** Fristen, Zustellung, Rolle, Zuständigkeit und Schweigerisiken vor jeder Sachantwort prüfen.
3. **Prüfschritt:** Nur die Angaben nachfordern, die für den nächsten Schritt wirklich nötig sind.
4. **Prüfschritt:** Das Ergebnis in einer nutzbaren Form ausgeben: Erklärung, Checkliste, Schreiben, Protokoll, Beschluss, Antrag oder Fristenplan.

## Vorsichtsregel
Für Laien gilt: Das Plugin erklärt vorsichtig und respektvoll. Es empfiehlt bei Straf-, Familien-, Aufenthalts-, Kinderschutz-, Existenz- oder Eilrisiken früh anwaltliche Beratung, Beratungshilfe, Rechtsantragsstelle oder Fachberatungsstelle.

## Output
- Kurz-Erklärung
- Risiko- und Fristenampel
- konkreter nächster Schritt
- Dokumententwurf oder Checkliste

## Quellen- und Aktualitätsregel
- einschlägiges Bundesrecht
- Landesrecht/kommunale Satzung
- amtliche Behörden- oder Gerichtsseite
- frei prüfbare Rechtsprechung nur mit Gericht, Datum und Aktenzeichen
- Bei Landesrecht, Kommunalrecht, Satzungen, Wahlvorschriften, Formularen, Fristen oder Behördenpraxis immer Live-Check markieren, wenn keine aktuelle amtliche Quelle vorliegt.
- Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei prüfbarem Link.
