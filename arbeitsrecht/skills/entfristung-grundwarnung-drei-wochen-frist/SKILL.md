---
name: entfristung-grundwarnung-drei-wochen-frist
description: "Grundwarnung Entfristungsklage: § 17 TzBfG drei Wochen ab vereinbartem Vertragsende; absolute Ausschlussfrist; § 17 Satz 2 TzBfG i.V.m. § 7 KSchG Fiktion Wirksamkeit der Befristung bei Fristversaeumnis; Fristberechnung; nachtraegliche Zulassung."
---

# Grundwarnung: Dreiwochenfrist § 17 TzBfG

## Zweck

Die Dreiwochenfrist des § 17 TzBfG ist die wichtigste und gefährlichste Frist im Entfristungsrecht. Sie läuft auch wenn man keinen Anwalt hat, auch wenn man noch weiterbeschäftigt wird, und auch wenn man von der Frist nichts weiß.

## Zentrale Normen

- § 17 TzBfG — Klagefrist 3 Wochen ab vereinbartem Vertragsende
- § 7 KSchG (analog) — Fiktionswirkung bei Fristversäumnis (Befristung gilt als wirksam)
- § 5 KSchG (analog) — Nachträgliche Zulassung bei unverschuldeter Versäumnis
- §§ 187, 188 BGB — Fristberechnung
- § 193 BGB — Verlängerung bei Wochenende/Feiertag
- § 15 Abs. 5 TzBfG — Unbefristetes Arbeitsverhältnis bei Weiterbeschäftigung ohne Widerspruch

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Die Norm — § 17 TzBfG (vollständig)

> **Satz 1:** Will der Arbeitnehmer geltend machen, dass die Befristung eines Arbeitsvertrags rechtsunwirksam ist, so muss er innerhalb von drei Wochen nach dem vereinbarten Ende des befristeten Arbeitsvertrags Klage beim Arbeitsgericht auf Feststellung erheben, dass das Arbeitsverhältnis auf Grund der Befristung nicht beendet ist.
>
> **Satz 2:** Die §§ 5 bis 7 des Kündigungsschutzgesetzes gelten entsprechend.

## Schritt-für-Schritt-Prüfung der Frist

### Schritt 1: Fristbeginn bestimmen

Die Frist beginnt mit dem **vereinbarten** Ende des Arbeitsvertrags (laut Vertragsurkunde), nicht dem tatsächlichen Ende.

**Fristbeginn-Entscheidungsbaum:**
```
Vertrag sagt: "befristet bis 31.03.2025"
→ Fristbeginn: 01.04.2025 (§ 187 Abs. 1 BGB — Anfangstag zählt nicht)
→ Fristende: 22.04.2025 um 24:00 Uhr (3 × 7 Tage = 21 Tage, §§ 188 Abs. 2, 187 Abs. 1 BGB)
→ Fällt 22.04.2025 auf Samstag/Sonntag/Feiertag: nächster Werktag (§ 193 BGB)
```

**Besonderheit Weiterbeschäftigung:**
Arbeitnehmer wird nach dem 31.03.2025 noch weiterbeschäftigt → Frist läuft trotzdem ab 01.04.2025. Weiterbeschäftigung hemmt den Fristlauf NICHT.

### Schritt 2: Fristende berechnen

```
Fristende = Vereinbartes Vertragsende + 1 Tag (§ 187 Abs. 1 BGB) + 21 Tage

Beispiel:
  Vereinbartes Ende: 31.03.2025
  Fristbeginn:       01.04.2025
  Fristende:         21.04.2025 (Montag) → letzter Tag für Klageeingang beim ArbG
```

### Schritt 3: Versäumnis feststellen?

**Ist die Frist bereits abgelaufen?**
- Ja → § 7 KSchG analog: Befristung gilt als wirksam. Nur noch nachträgliche Zulassung (§ 5 KSchG) möglich.
- Nein → Sofort Klage erheben (Skill: `entfristung-klageschrift-laie-baustein` oder `entfristung-klageschrift-anwalt-baustein`)

### Schritt 4: Nachträgliche Zulassung prüfen (§ 5 KSchG analog)

Falls Frist versäumt:
- War die Versäumnis unverschuldet? (z.B. schwere Krankheit, Naturkatastrophe, fehlerhafter Behördenrat)
- Frist für Zulassungsantrag: 2 Wochen nach Wegfall des Hindernisses
- Antrag gleichzeitig mit der Klage einreichen
- Prüfungsmaßstab: streng — bloße Rechtsunkenntnis genügt nicht

## Entscheidungsbaum

```
Ist Frist noch nicht abgelaufen?
├── Ja → Klage sofort einreichen → entfristung-klageschrift-laie/anwalt-baustein
└── Nein → War Versäumnis unverschuldet?
    ├── Ja → Antrag auf nachträgliche Zulassung (§ 5 KSchG) + Klage gleichzeitig
    └── Nein → Befristung gilt als wirksam (§ 7 KSchG) — kein Rechtsmittel mehr
```

## Sofortprüfungs-Checkliste (Abfrage an Nutzer)

1. Wann endet der Vertrag laut Vertragsurkunde? (Datum exakt)
2. Ist dieses Datum bereits abgelaufen?
3. Falls abgelaufen: seit wie vielen Tagen?
4. Wurde Klage bereits erhoben?
5. Wird der Arbeitnehmer noch weiterbeschäftigt?

## Besonderheit: Mehrere Befristungen

Bei aufeinanderfolgenden befristeten Verträgen:
- Jeder Vertrag hat seine eigene Frist
- Die Frist beginnt mit dem Ende des **jeweils letzten Vertrags**
- Frühere Verträge können nach Fristablauf nicht mehr angegriffen werden
- **Konsequenz:** Bei mehrfacher Verlängerung läuft die Frist nur beim letzten Vertrag

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Sachverhaltsangabe oder falsche Anspruchsgrundlage entwertet das Ergebnis. Dringende Empfehlung anwaltlicher Beratung, insbesondere wegen der Drei-Wochen-Fristen.

Du könntest auf der falschen Wiese unterwegs sein. Dieses System kann das nicht prüfen.
