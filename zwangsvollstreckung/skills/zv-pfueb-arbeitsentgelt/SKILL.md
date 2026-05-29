---
name: zv-pfueb-arbeitsentgelt
description: "Gläubiger will Lohn oder Gehalt des Schuldners pfaenden lassen. §§ 829 835 850 ff. ZPO Lohnpfaendung PfUeB. Prüfraster: PfUeB gegen Arbeitgeber als Drittschuldner pfaendbarer Betrag Pfaendungstabelle 1.7.2025 bis 30.6.2026 Unterhaltsberechtigte Sonderzuwendungen § 850a ZPO Anschlusspfaendungen § 850e ZPO. Output: PfUeB-Antrag Lohn fertig zum Einreichen. Abgrenzung zu zv-pfueb-bank (Konto) und zv-pfaendungstabelle-2025 (reine Berechnung)."
---

# PfÜB Arbeitsentgelt

## Aufgabe

Pfändung des laufenden Arbeitseinkommens. Bauteil mit den meisten Stolpersteinen: Pfändungstabelle, Unterhalt, Sonderzuwendungen, Krankengeld, Arbeitgeberwechsel.

## Startet bei

- Titel + Klausel + Zustellung grün
- Arbeitgeber bekannt (sonst `zv-vermoegensauskunft-gv`)
- Schuldner nicht in Insolvenz

## Rechtsgrundlagen

- §§ 829, 835 ZPO – Pfändung und Überweisung
- § 850 ZPO – Pfändbarkeit von Arbeitseinkommen
- § 850a ZPO – unpfändbare Bezüge (50 % Mehrarbeit, voll Urlaubsgeld, Weihnachten bis Hälfte des Monatsverdienstes, Aufwand)
- § 850c ZPO – Pfändungsfreigrenze, Tabelle des BMJ; aktuelle Bekanntmachung 1.7.2025
- § 850d ZPO – privilegierte Unterhaltsforderungen, abweichende Berechnung
- § 850e ZPO – Zusammenrechnung mehrerer Einkommen
- § 850f ZPO – Erhöhung des Freibetrags durch Vollstreckungsgericht
- § 850k ZPO – nur mittelbar (Auszahlung auf P-Konto)
- § 87 InsO bei laufender Insolvenz

## Workflow

1. **Drei-Säulen-Prüfung**.
2. **Arbeitgeber als Drittschuldner** bezeichnen – nicht "die Firma X", sondern die juristische Person.
3. **Forderung** definieren: laufendes Arbeitseinkommen, einschließlich künftiger Erhöhungen, einschließlich Sonderzuwendungen soweit pfändbar.
4. **Berechnung pfändbarer Betrag** mit `werkzeuge/pfaendungsrechner.py` (Tabelle 1.7.2025): Nettoeinkommen → unterhaltsberechtigte Personen → Pfändbarkeitsstufe.
5. **Privilegierte Unterhaltsforderung** § 850d ZPO: deutlich niedrigerer Freibetrag, vom Vollstreckungsgericht festzusetzen.
6. **Antragsformular** ZVFV nutzen. Ab 1.10.2026 neue Muster und XML-Antrag möglich.
7. **Einreichen** beim Vollstreckungsgericht am Schuldnerwohnsitz.
8. **Zustellung** an Arbeitgeber durch Gerichtsvollzieher (Papier) oder elektronisch.
9. **Drittschuldnererklärung § 840 ZPO** abwarten.
10. **Anschlusspfändung** prüfen, wenn weitere Gläubiger pfänden (Rangfrage § 804 Abs. 3 ZPO).

## Pfändungstabelle 1.7.2025

Gültig seit 1.7.2025 (Bekanntmachung BMJ). Die Tabelle wird zum 1.7. jeden ungeraden Jahres neu festgesetzt – nächste Fortschreibung 1.7.2027. Aktuelle Werte stehen in `werkzeuge/pfaendungsrechner.py`. Faustwerte: Freibetrag ohne Unterhalt rund 1.560 EUR netto, mit einem Unterhaltsberechtigten rund 2.150 EUR.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
PFÜB ARBEITSENTGELT [Mandant] gegen [Schuldner], Az [Gericht]

Titel:                 [Art, Datum, Aussteller]
Forderung:             EUR Haupt + EUR Zinsen + EUR Kosten
Drittschuldner:        [Arbeitgeber als juristische Person]
Schuldner-Netto:       EUR x (zuletzt bekannter Wert, Datum)
Unterhaltspflichten:   [Anzahl]
Pfändbarer Betrag:     EUR y / Monat (Tabelle 1.7.2025)
Privileg § 850d:       [ja – Unterhaltsforderung / nein]
Sonderzuwendungen:     [erfasst nach § 850a Nr. 3/4 ZPO]

NÄCHSTER SCHRITT:      Drittschuldnererklärung in 2 Wochen
WIEDERVORLAGE:         DD.MM.JJJJ
```

## Qualitätsgates

- Niemals Bruttoeinkommen pfänden – pfändbar ist der Nettoteil.
- Niemals Sonderzuwendungen § 850a ZPO ohne Prüfung in den pfändbaren Teil rechnen.
- Bei mehreren Einkommen (Lohn + Rente, Lohn + Selbstständigkeit) Zusammenrechnung § 850e ZPO ausdrücklich beantragen.
- Bei privilegierten Unterhaltsforderungen § 850d ZPO eigene Festsetzung beantragen.
- Bei Sterbe-/Krankengeld besondere Pfändbarkeitsgrenzen prüfen.

<!-- AUDIT 27.05.2026
Geprüft: 3 AZ aus task_259.json
- BGH VII ZB 16/12: NOT_FOUND auf dejure.org → gelöscht
- BGH VII ZB 17/05: WRONG_TOPIC (real: § 850f Abs. 2 ZPO Vollstreckungsprivileg, nicht § 850a Nr. 4) → Beschreibung korrigiert
-->

## Querverweise

- `zv-pfaendungstabelle-2025` – Rechentool
- `zv-titel-klausel-zustellung` – Vorprüfung
- `zv-vermoegensauskunft-gv` – wenn Arbeitgeber unbekannt
- `zv-elektronische-zustellung-2027` – ERV-Stand
- `zv-abwehr-schuldner` – Schuldnersicht
