# 16 — Finding 9: Abweichende Makroausführung VBA

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Finding-ID:** F-09
**Schwere:** Hoch
**Entdeckt:** 13. Januar 2026

---

## Sachverhalt

Das Modell v23 enthält ein VBA-Modul (`Module1`) mit der Prozedur `UpdateSollwerte`. Laut Metadaten wurde das Modul zuletzt am 04. Januar 2026 (einen Tag vor dem offiziellen Modellstand v23) gespeichert.

### Makroinhalt (rekonstruiert)

```vba
Sub UpdateSollwerte()
    ' Sollwerte bei Dateiöffnung setzen
    Sheets("PLAN-GuV").Range("E22").Value = 0.072
    Sheets("PLAN-GuV").Range("F22").Value = 0.072
    Sheets("LIQUIDITAET").Range("D11").Value = 350000
    Sheets("PLAN-CF").Range("H8").Value = 42
End Sub
```

Das Makro wird beim Öffnen der Datei (`Workbook_Open`) ausgeführt und überschreibt Zellen in `PLAN-GuV` und `LIQUIDITAET` mit festen Werten. Diese Werte entsprechen den unter Finding 2 dokumentierten Hardcoded-Werten.

---

## Auswirkung

Die Makroausführung bewirkt, dass:
- Formelkorrekturen in den betroffenen Zellen beim nächsten Dateiöffnen überschrieben werden.
- Ein externer Prüfer, der die Formel in `PLAN-GuV!E22` korrigiert und die Datei speichert, beim erneuten Öffnen wieder den Makrowert vorfindet.
- Die im Modell sichtbaren Hardcoded-Werte nicht manuell eingetragen, sondern durch das Makro gesetzt wurden — was die Änderungsnachvollziehbarkeit weiter erschwert.

---

## Rechtliche Relevanz

Ein Makro, das bei jedem Öffnen Planwerte überschreibt und damit die Wirkung externer Korrekturen neutralisiert, ist mit den Anforderungen an ein transparentes, nachvollziehbares Planungsmodell unvereinbar. Im Kontext der übrigen Findings (insbesondere F-04, Manipulationsverdacht) verstärkt dieser Befund den Gesamtverdacht erheblich.

---

## Empfehlung

Sofortige Deaktivierung und Löschung des Makros. Dokumentation der durch das Makro gesetzten Werte und ihrer Entstehungshistorie. Prüfung durch Wirtschaftsprüfer Birkholz & Partner, ob das Makro Einfluss auf bisher vorgelegte Prüfungsversionen hatte.

**Verantwortlich:** CFO Pellbach-Roosendaal; GF Dr. Vellbruck-Steinheim (Haftungsverantwortung).
**Frist:** Sofort (vor jeder weiteren Verteilung des Modells).

**Quellen:** StGB § 267 (Urkundenfälschung, mittelbar): [https://dejure.org/gesetze/StGB/267.html](https://dejure.org/gesetze/StGB/267.html); HGB § 239 Abs. 3 (Unveränderbarkeit von Buchführungsunterlagen), [https://dejure.org/gesetze/HGB/239.html](https://dejure.org/gesetze/HGB/239.html).
