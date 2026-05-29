---
name: fristen-und-terminkalender
description: "Anwalt will alle prozessrelevanten Fristen und Termine im Aktenauszug hervorheben: Klagefrist Berufungsfrist Begründungsfrist Verkündungstermin Vollziehungsfrist. Normen §§ 222 517 520 548 ZPO. Prüfraster Vollständigkeit Frist-Berechnung Hervorhebung Fehler-Scan. Output Fristen-Box Fristen-Tabelle. Abgrenzung zu verfahrenschronologie (Prozessschritte) und mittelstand-ma-fristen-cp-kalender (M&A-Fristen)."
---

# Fristen und Terminkalender

## Zweck

Versäumte Fristen können zum Verlust des Verfahrens oder zur Haftung des Rechtsanwalts führen. Dieser Skill identifiziert alle prozessrelevanten Fristen und Termine aus der Akte und stellt sie prominent dar.

## Triage — kläre vor Fristermittlung

1. Wurde das Urteil (erstinstanzlich) bereits zugestellt? (Berufungsfrist läuft!)
2. Liegt ein Hinweisbeschluss des Gerichts mit Frist vor?
3. Wurden Sachverständigenvorschüsse angefordert mit Zahlungsfrist?
4. Handelt es sich um ein Eilverfahren? (Vollziehungsfrist § 929 Abs. 2 ZPO)
5. KSchG-Verfahren? (3-Wochen-Frist § 4 KSchG — absolute Notfrist)

## Zentrale Normen

- § 222 ZPO i.V.m. §§ 187-188 BGB — Fristberechnung (Wochenende, Feiertag)
- § 233-238 ZPO — Wiedereinsetzung in den vorigen Stand bei unverschuldetem Fristversäumnis
- § 517 ZPO — Berufungsfrist 1 Monat; § 520 Abs. 2 ZPO — Begründungsfrist 2 Monate
- § 548 ZPO — Revisionsfrist 1 Monat; § 551 ZPO — Revisionsbegründungsfrist 2 Monate
- § 929 Abs. 2 ZPO — Vollziehungsfrist einstweilige Verfügung 1 Monat
- § 4 KSchG — Klagefrist 3 Wochen (Notfrist); § 74 VwGO — Klagefrist 1 Monat

## Rechtsprechung zu Fristen und Fristversäumnis

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Fristenarten

### Absolute Fristen (gesetzlich, nicht verlängerbar)

| Frist | Norm | Fristdauer | Berechnung |
|---|---|---|---|
| Berufungsfrist | § 517 ZPO | 1 Monat | ab Zustellung Urteil |
| Berufungsbegründungsfrist | § 520 Abs. 2 ZPO | 2 Monate | ab Zustellung Urteil |
| Revisionsfrist | § 548 ZPO | 1 Monat | ab Zustellung Urteil |
| Revisionsbegründungsfrist | § 551 ZPO | 2 Monate | ab Zustellung Urteil |
| Klagefrist KSchG | § 4 KSchG | 3 Wochen | ab Zugang Kündigung |
| Klagefrist VwGO | § 74 VwGO | 1 Monat | ab Zustellung Widerspruchsbescheid |
| Vollziehungsfrist eV | § 929 Abs. 2 ZPO | 1 Monat | ab Zustellung Beschluss |
| Berufungsfrist ArbGG | § 66 ArbGG | 1 Monat | ab Zustellung Urteil |
| Berufungsfrist SGG | § 151 SGG | 1 Monat | ab Zustellung Urteil |

### Richterliche Fristen (verlängerbar)

- Schriftsatzfristen des Gerichts (Klageerwiderung, Replik, Duplik)
- Frist zur Stellungnahme zu Hinweisbeschlüssen
- Frist zur Einzahlung von Auslagen (Sachverständigenvorschuss)

### Notfristen

Fristen, die nicht verlängerbar sind und bei denen Wiedereinsetzung nur unter engen Voraussetzungen möglich ist (z. B. Berufungsfrist).

## Output-Format (Fristenbox am Anfang)

```
FRISTEN UND TERMINE — SOFORT PRUEFEN
Berufungsfrist:    TT.MM.JJJJ  (§ 517 ZPO)
Begründungsfrist:  TT.MM.JJJJ  (§ 520 ZPO)
Nächste Verhandlung: TT.MM.JJJJ HH:UU Uhr
Schriftsatzfrist:  TT.MM.JJJJ  (richterliche Anordnung)
```

Alternativ als Markdown-Tabelle:

```markdown
## Fristen und Termine — Sofort prüfen

| Frist / Termin | Datum | Norm | Status |
|---|---|---|---|
| Berufungsfrist | TT.MM.JJJJ | § 517 ZPO | laeuft |
| Begründungsfrist | TT.MM.JJJJ | § 520 ZPO | laeuft |
| Mündliche Verhandlung | TT.MM.JJJJ | Terminsverfügung | angesetzt |
```

## Berechnungshinweise

- Fristbeginn immer anhand des tatsächlichen Zustellungsdatums aus der Akte ermitteln
- Wenn Zustellungsdatum nicht bekannt: ausdrücklich als "Zustellungsdatum unbekannt — Frist nicht berechenbar" kennzeichnen
- Wochenenden und gesetzliche Feiertage nach § 222 ZPO i.V.m. §§ 187-188 BGB berücksichtigen
- Bei Monatsfristen: Fristende = gleicher Tag des Folgemonats (§ 188 Abs. 2 BGB)

## Qualitätscheck

- [ ] Alle gesetzlichen Fristen aus der Akte erfasst?
- [ ] Fristenbox am Anfang des Aktenauszugs?
- [ ] Berechnungsgrundlage (Zustellungsdatum) angegeben?
- [ ] Fehlende Zustellungsdaten als "unbekannt" markiert?
- [ ] Fristen in der Verfahrenschronologie markiert?
- [ ] Wochenende/Feiertag bei Fristende berücksichtigt (§ 222 ZPO)?

---
