# 13 — Finding 6: Versteckte Blätter mit Restposten

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Finding-ID:** F-06
**Schwere:** Hoch
**Entdeckt:** 12. Januar 2026

---

## Sachverhalt

Das Modell `PFX-FoBP-Modell-v23-final.xlsx` enthält neben den 16 sichtbaren Arbeitsblättern zwei versteckte Blätter:

### Blatt 1: `_BACKUP_PARAM` (sehr versteckt, xlSheetVeryHidden)

- Enthält Parametersätze aus Modell v19 (August/September 2025).
- Keine aktiven Verknüpfungen zu anderen Blättern (verwaiste Daten).
- Zinssatz in `_BACKUP_PARAM!B12`: 7,1 % — deutlich höher als aktuell verwendete 4,9 %.
- Kein Risiko für aktuelle Berechnungen, aber dokumentarisch bedeutsam (zeigt früheren Zinssatz).

### Blatt 2: `_RESTPOSTEN` (sehr versteckt, xlSheetVeryHidden)

- Enthält eine Tabelle mit 14 nicht aufgelösten Differenzposten aus Versionsübergängen v19–v22.
- Gesamtsumme der Restposten: 87 TEUR (Passivaüberhang).
- Drei Positionen sind als Formelverweise auf `PLAN-BILANZ` verknüpft und beeinflussen indirekt die Bilanzsummenberechnung (obwohl das Blatt versteckt ist, sind die Bezüge aktiv).

---

## Auswirkung

Die aktiven Verknüpfungen aus `_RESTPOSTEN` in `PLAN-BILANZ` bedeuten, dass Teile der Bilanzsummenberechnung von einem für den Prüfer nicht sichtbaren Blatt abhängen. Dies verletzt fundamentale Transparenzanforderungen.

Der Passivaüberhang von 87 TEUR aus `_RESTPOSTEN` ist in der ausgewiesenen Bilanzsumme enthalten, ohne dass er separat erklärt oder gerechtfertigt wird.

---

## Rechtliche Relevanz

Die Verwendung versteckter Blätter mit aktiven Verknüpfungen in einem Dokument, das als Grundlage für Kreditentscheidungen und Jahresabschlussprüfung dient, ist mit den Anforderungen an Transparenz und Nachvollziehbarkeit gemäß IDW S 11 unvereinbar. Im Kontext des Manipulationsverdachts (Finding 4) verstärkt dieser Befund den Gesamteindruck mangelhafter Modellintegrität.

---

## Empfehlung

Sofortige Offenlegung beider versteckter Blätter gegenüber dem Wirtschaftsprüfer. Auflösung aller aktiven Verknüpfungen aus `_RESTPOSTEN`. Entscheidung über Einbeziehung oder Deletion beider Blätter mit Dokumentation.

**Verantwortlich:** CFO Pellbach-Roosendaal.
**Frist:** 1 Arbeitstag.

**Quellen:** IDW S 11 Tz. 22 (Transparenz und Nachvollziehbarkeit), [https://www.idw.de](https://www.idw.de); HGB § 239 (Buchführungsgrundsätze), [https://dejure.org/gesetze/HGB/239.html](https://dejure.org/gesetze/HGB/239.html).
