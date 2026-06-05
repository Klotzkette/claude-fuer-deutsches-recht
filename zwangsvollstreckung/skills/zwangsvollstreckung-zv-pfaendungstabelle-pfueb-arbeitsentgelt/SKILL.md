---
name: zwangsvollstreckung-zv-pfaendungstabelle-pfueb-arbeitsentgelt
description: "ZV Pfaendungstabelle Pfueb Arbeitsentgelt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ZV Pfaendungstabelle Pfueb Arbeitsentgelt

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **ZV Pfaendungstabelle Pfueb Arbeitsentgelt** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zv-pfaendungstabelle-2025` | Lohnpfaendung oder Rentenpfaendung ist beantragt und der pfaendbare Betrag muss konkret berechnet werden. Pfaendungsfreigrenzenbekanntmachung 1.7.2025 gueltig bis 30.6.2026. Prüfraster: Freibetrag § 850c ZPO Unterhaltsstaffel Pfaendungsstufen P-Konto-Sockel § 850k ZPO privilegierte Berechnung § 850d ZPO Unterhalt. Output: Berechnungsprotokoll pfaendbarer Betrag mit Stufen. Abgrenzung zu zv-pfueb-arbeitsentgelt (PfUeB-Antrag) und zv-pfueb-bank (Kontopfaendung). |
| `zv-pfueb-arbeitsentgelt` | Gläubiger will Lohn oder Gehalt des Schuldners pfaenden lassen. §§ 829 835 850 ff. ZPO Lohnpfaendung PfUeB. Prüfraster: PfUeB gegen Arbeitgeber als Drittschuldner pfaendbarer Betrag Pfaendungstabelle 1.7.2025 bis 30.6.2026 Unterhaltsberechtigte Sonderzuwendungen § 850a ZPO Anschlusspfaendungen § 850e ZPO. Output: PfUeB-Antrag Lohn fertig zum Einreichen. Abgrenzung zu zv-pfueb-bank (Konto) und zv-pfaendungstabelle-2025 (reine Berechnung). |
| `zv-pfueb-bank` | Gläubiger will Bankkonto des Schuldners pfaenden lassen. §§ 829 835 ZPO PfUeB Bankkonten. Prüfraster: Antrag Drittschuldner-Bank P-Konto-Schutz § 850k ZPO Sockelbetrag Kindergeld Erhöhungen ZVollstrDigitG XML-Antrag ab 1.10.2026 elektronische Zustellung ab 1.10.2027. Output: PfUeB-Antrag Konto fertig zum Einreichen. Abgrenzung zu zv-pfueb-arbeitsentgelt (Lohn) und zv-eu-kontenpfaendung-655-2014 (Auslands-Konto). |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **ZV Pfaendungstabelle Pfueb Arbeitsentgelt**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zv-pfaendungstabelle-2025`

**Fokus:** Lohnpfaendung oder Rentenpfaendung ist beantragt und der pfaendbare Betrag muss konkret berechnet werden. Pfaendungsfreigrenzenbekanntmachung 1.7.2025 gueltig bis 30.6.2026. Prüfraster: Freibetrag § 850c ZPO Unterhaltsstaffel Pfaendungsstufen P-Konto-Sockel § 850k ZPO privilegierte Berechnung § 850d ZPO Unterhalt. Output: Berechnungsprotokoll pfaendbarer Betrag mit Stufen. Abgrenzung zu zv-pfueb-arbeitsentgelt (PfUeB-Antrag) und zv-pfueb-bank (Kontopfaendung).

# Pfändungstabelle 1.7.2025

## Triage zu Beginn

1. Handelt es sich um Arbeitseinkommen (§ 850c ZPO) oder selbstständiges Einkommen (§ 850i ZPO)?
2. Wie viele unterhaltsberechtigte Personen sind zu berücksichtigen?
3. Handelt es sich um privilegierte Unterhaltspfändung (§ 850d ZPO) oder reguläre Pfändung?
4. Hat der Schuldner ein P-Konto — wenn ja, Sockelbetrag und Erhöhungen (§ 850k ZPO) berechnen?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 850a ZPO — Unpfändbare Bezüge (Sonderzuwendungen, Aufwandsentschädigungen)
- § 850c ZPO — Pfändungsfreigrenze (Tabelle, jährlich angepasst)
- § 850d ZPO — privilegierte Unterhaltspfändung (geringerer Selbstbehalt)
- § 850f ZPO — Erhöhung durch Gericht aus persönlichen Gründen
- § 850i ZPO — Pfändung bei selbstständigem Einkommen
- § 850k ZPO — Pfändungsschutzkonto (P-Konto), Sockelbetrag und Erhöhungen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Verlässlich pfändbare Beträge berechnen. Falsche Pfändungsfreigrenzen sind der häufigste Vollstreckungsfehler – Skill kapselt die aktuelle Tabelle und das zugehörige Python-Werkzeug.

## Startet bei

- Lohnpfändung in Vorbereitung (`zv-pfueb-arbeitsentgelt`)
- Kontopfändung mit P-Konto-Berechnung (`zv-pfueb-bank` + § 850k ZPO)
- Schuldnerseite verlangt Anpassung der Freibeträge (`zv-abwehr-schuldner`)

## Rechtsgrundlagen

- § 850c ZPO – Pfändungsfreigrenze für Arbeitseinkommen
- § 850d ZPO – Unterhaltsforderungen (privilegiert, geringerer Freibetrag, vom Gericht festgesetzt)
- § 850f ZPO – Erhöhung durch Gericht aus persönlichen Gründen
- § 850k ZPO – Pfändungsschutzkonto, Sockelbetrag und Erhöhungen
- Pfändungsfreigrenzenbekanntmachung 2025 vom 11.4.2025 (BGBl. 2025 I Nr. 110), in Kraft 01.07.2025 bis 30.06.2026
- Quelle BGBl.: https://www.recht.bund.de/bgbl/1/2025/110/VO.html
- Quelle gesetze-im-internet: https://www.gesetze-im-internet.de/pf_ndfreigrbek_2025/BJNR06E0A0025.html
- nächste Anpassung 01.07.2026 (§ 850c Abs. 4 ZPO – jährlich am 1. Juli entsprechend der Entwicklung des Grundfreibetrags § 32a EStG)

## Gültigkeit der aktuellen Tabelle

Die Bekanntmachung gilt vom **1.7.2025 bis 30.6.2026**. Die nächste Anpassung erfolgt zum 1.7.2026 (§ 850c Abs. 4 ZPO jährlich). Der Skill prüft bei jeder Berechnung das Tagesdatum – nach dem 30.6.2026 muss `werkzeuge/pfaendungsrechner.py` aktualisiert werden.

> ⚠️ **Auto-Warnung ab 1.6.2026:** Wenn das System-Datum innerhalb von 30 Tagen vor Ablauf der Tabelle (≥ 1.6.2026) liegt, gibt der Skill und das Werkzeug einen Warntext aus, dass eine neue Pfändungsfreigrenzenbekanntmachung des BMJ veröffentlicht und in die Tabelle übernommen werden muss. Pflicht-Quellen: Pfändungsfreigrenzenbekanntmachung 2026 (BGBl. I); BMJ-Pressemitteilung; Konsultation in `juris`/`beck-online`. Verwendung der alten Eckwerte nach 30.6.2026 = Pfändungsfehler mit Aufhebungspotential.

## Eckwerte (aus Tabelle, dezimal mit Punkt)

Aktuelle Eckdaten (Tabelle 01.07.2025 bis 30.06.2026, BGBl. 2025 I Nr. 110):

- Grundfreibetrag ohne Unterhaltspflichten: 1.555,00 EUR netto / Monat (§ 850c Abs. 1 Nr. 1 ZPO i.V.m. Pfändungsfreigrenzenbekanntmachung 2025).
- Erhöhung erste unterhaltsberechtigte Person: 585,23 EUR (§ 850c Abs. 2 Satz 1 ZPO).
- Erhöhung jede weitere Person (2. bis 5. Person): 326,04 EUR (§ 850c Abs. 2 Satz 2 ZPO).
- Vollpfändungsgrenze: 4.766,99 EUR (§ 850c Abs. 3 Satz 3 ZPO).
- Netto wird vor Berechnung auf den nächsten vollen 10-EUR-Schritt abgerundet (§ 850c Abs. 5 ZPO).
- P-Konto-Sockel § 850k ZPO: 1.560,00 EUR (AG SBV-Bescheinigung Stand 01.07.2025).
- Pfändbarer Betrag wird nach unten gerundet (§ 850c Abs. 5 ZPO i.V.m. Tabellenmethode).
- Alle exakten Werte im `werkzeuge/pfaendungsrechner.py` (Single Source of Truth).

Steigerung gegenueber Vorjahresfassung:

- Grundfreibetrag von 1.491,75 EUR auf 1.555,00 EUR
- Erhoehungsbetrag 1. Unterhaltspflicht von 561,43 EUR auf 585,23 EUR
- Vollpfaendungsgrenze von 4.573,10 EUR auf 4.766,99 EUR

Die Werte sind dimensions- und kommageführt im Werkzeug Single-Source-of-Truth; dieses SKILL.md nennt sie zur Orientierung. Komma-Zahlen sind im Body erlaubt, nicht im Frontmatter `description`.

## Workflow

1. **Inputs einholen**: Nettoeinkommen, Anzahl unterhaltsberechtigter Personen, ggf. Sonderzuwendungen, Privileg § 850d ZPO ja/nein.
2. **Python-Werkzeug aufrufen**: `python zwangsvollstreckung/werkzeuge/pfaendungsrechner.py --netto 2500 --unterhalt 1`.
3. **Output**: Freibetrag, pfändbarer Betrag, Pfändungsstufen, Hinweise zu § 850a ZPO Sonderzuwendungen.
4. **§ 850d ZPO privilegiert**: separat berechnen lassen mit `--privileg unterhalt --selbstbehalt 1450` o.ä.
5. **P-Konto** § 850k ZPO: Sockel und Erhöhungsbeträge ausgeben.
6. **Antragstext** für den PfÜB ergänzen.

## Privilegierte Unterhaltspfändung § 850d ZPO

- Selbstbehalt wird vom Vollstreckungsgericht festgelegt – Werte orientieren sich an der Düsseldorfer Tabelle (Selbstbehalt aktuell 1.450 EUR Erwerbstätiger gegenüber minderjährigen Kindern, Stand Tabelle 2025).
- Skill gibt eine Größenordnung an, weist aber auf die richterliche Festsetzung hin.

## P-Konto-Schutz § 850k ZPO – Erhöhungen

Erhöhungen müssen durch Bescheinigung (Schuldnerberatung, anerkannter Berater, Arbeitgeber, Familienkasse, Sozialleistungsträger) belegt werden:

- pro unterhaltsberechtigter Person
- Kindergeld
- einmalige Sozialleistungen
- Nachzahlungen

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
PFÄNDUNGSBERECHNUNG (Tabelle 1.7.2025)

Netto: EUR x
Unterhaltspflichten: n
Pfändbar regulär: EUR y / Monat
Pfändbar privilegiert: EUR z (§ 850d ZPO, Selbstbehalt EUR a)
P-Konto-Sockel: EUR b / Monat (+ Erhöhungen)
Hinweis Sonderzuw.: [§ 850a Nr. 3/4 ZPO]

Tabelle gültig bis: 30.6.2027
```

## Qualitätsgates

- Niemals Tabellenwerte 2019, 2021, 2022, 2023 verwenden.
- Niemals Bruttobetrag in die Tabelle einsetzen.
- Niemals § 850d ZPO ohne richterliche Festsetzung als feste Zahl ausgeben.
- Bei selbstständigem Einkommen Berechnung § 850i ZPO statt § 850c ZPO.
- Bei Sozialleistungen § 54 SGB I prüfen.

## Querverweise

- `zv-pfueb-arbeitsentgelt`, `zv-pfueb-bank`
- `zv-abwehr-schuldner`
- `werkzeuge/pfaendungsrechner.py`
- `forderungsmanagement-klagewerkstatt/skills/inkasso-zahlungsklage-ersteller`

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:

## 2. `zv-pfueb-arbeitsentgelt`

**Fokus:** Gläubiger will Lohn oder Gehalt des Schuldners pfaenden lassen. §§ 829 835 850 ff. ZPO Lohnpfaendung PfUeB. Prüfraster: PfUeB gegen Arbeitgeber als Drittschuldner pfaendbarer Betrag Pfaendungstabelle 1.7.2025 bis 30.6.2026 Unterhaltsberechtigte Sonderzuwendungen § 850a ZPO Anschlusspfaendungen § 850e ZPO. Output: PfUeB-Antrag Lohn fertig zum Einreichen. Abgrenzung zu zv-pfueb-bank (Konto) und zv-pfaendungstabelle-2025 (reine Berechnung).

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

Titel: [Art, Datum, Aussteller]
Forderung: EUR Haupt + EUR Zinsen + EUR Kosten
Drittschuldner: [Arbeitgeber als juristische Person]
Schuldner-Netto: EUR x (zuletzt bekannter Wert, Datum)
Unterhaltspflichten: [Anzahl]
Pfändbarer Betrag: EUR y / Monat (Tabelle 1.7.2025)
Privileg § 850d: [ja – Unterhaltsforderung / nein]
Sonderzuwendungen: [erfasst nach § 850a Nr. 3/4 ZPO]

NÄCHSTER SCHRITT: Drittschuldnererklärung in 2 Wochen
WIEDERVORLAGE: DD.MM.JJJJ
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

## 3. `zv-pfueb-bank`

**Fokus:** Gläubiger will Bankkonto des Schuldners pfaenden lassen. §§ 829 835 ZPO PfUeB Bankkonten. Prüfraster: Antrag Drittschuldner-Bank P-Konto-Schutz § 850k ZPO Sockelbetrag Kindergeld Erhöhungen ZVollstrDigitG XML-Antrag ab 1.10.2026 elektronische Zustellung ab 1.10.2027. Output: PfUeB-Antrag Konto fertig zum Einreichen. Abgrenzung zu zv-pfueb-arbeitsentgelt (Lohn) und zv-eu-kontenpfaendung-655-2014 (Auslands-Konto).

# PfÜB Bankkonto

## Aufgabe

Pfändung und Überweisung einer Forderung des Schuldners gegen sein Kreditinstitut. Dies ist die häufigste Geldvollstreckung und gleichzeitig der Bereich, in dem das ZVollstrDigitG 2026/2027 die größten Praxisänderungen bringt.

## Startet bei

- Vollstreckbarer Titel liegt vor (Drei-Säulen-Prüfung grün – sonst zurück an `zv-titel-klausel-zustellung`).
- Bankverbindung des Schuldners bekannt **oder** zu ermitteln (dann erst `zv-kontensuche-drittschuldner`).
- Schuldner nicht in Insolvenz (§ 89 InsO – sonst Stop).

## Rechtsgrundlagen

- § 829 ZPO – Pfändung einer Geldforderung
- § 835 ZPO – Überweisung an Zahlungs statt oder zur Einziehung
- § 833a ZPO – Pfändung eines Kontoguthabens, Moratorium von vier Wochen
- § 850k ZPO – Pfändungsschutzkonto (P-Konto)
- § 850c ZPO – Pfändungsfreigrenze für Arbeitseinkommen (mittelbar bei Lohnüberweisung)
- § 840 ZPO – Drittschuldnererklärung
- § 173 ZPO n.F. (ZVollstrDigitG) – elektronische Zustellung an Kreditinstitute
- Pfändungsfreigrenzenbekanntmachung 2025

## Workflow

1. **Titel + Klausel + Zustellung** prüfen lassen.
2. **Drittschuldner** identifizieren: Bank, IBAN reicht nicht – Bank ist der Drittschuldner, IBAN nur Bezeichnung des Anspruchs.
3. **Antrag bauen** an das Vollstreckungsgericht am Wohnsitz des Schuldners (§ 828 Abs. 2 ZPO). Pflichtangaben:
 - Gläubiger, Schuldner, Drittschuldner-Bank
 - Forderungsaufstellung (Hauptforderung, Zinsen, Kosten, Verzugskosten)
 - genaue Bezeichnung der gepfändeten Forderung ("gesamtes Guthaben sowie alle künftigen Eingänge auf jedem Konto, das der Schuldner bei der Drittschuldnerin unterhält")
 - Auskunftsersuchen § 840 ZPO
4. **Formular** verwenden – Pflichtformular der ZVFV. Ab 1.10.2026 neue Muster (vereinheitlicht, XML-Anhang).
5. **Einreichen** beim Vollstreckungsgericht: derzeit Papier oder elektronisch über beA/eBO. Ab 1.10.2026 XML-Antrag nach § 829 Abs. 5 ZPO n.F. möglich (PDF + maschinenlesbare XML, XML führend).
6. **Zustellung an Drittschuldner** und Schuldner:
 - bis 30.9.2027: per Gerichtsvollzieher (Papier) oder freiwillig elektronisch
 - ab 1.10.2027: Kreditinstitute MÜSSEN sicheren Übermittlungsweg eröffnen – Pfändungen werden in der Regel elektronisch über eBO oder § 130a Abs. 4 ZPO zugestellt
7. **Drittschuldnererklärung § 840 ZPO** abwarten (zwei Wochen). Reaktion auswerten: gepfändet, gesperrt, P-Konto, andere Pfändung vorrangig.
8. **P-Konto-Schutz prüfen**: Schuldner kann binnen vier Wochen nach Zustellung Umwandlung zum P-Konto verlangen, dann Sockelbetrag § 850k ZPO frei. Erhöhungsbeträge nach § 850k Abs. 2 ZPO.
9. **Auszahlung** ggf. nach Ablauf des Moratoriums § 833a ZPO (vier Wochen) – Verbraucher kann in dieser Zeit Vollstreckungsschutz beantragen.

## Reform-Stand ZVollstrDigitG (Stand 25.5.2026)

| Datum | Was ändert sich |
| --- | --- |
| 1.10.2026 | Neue ZVFV-Formulare, § 829 Abs. 5 ZPO n.F. XML-Antrag (PDF + XML, XML führend). Banken dürfen schon jetzt freiwillig elektronisch annehmen. |
| 1.10.2027 | Kreditinstitute MÜSSEN sicheren Übermittlungsweg nach § 130a Abs. 4 ZPO eröffnen (§ 173 Abs. 2 Nr. 1 ZPO n.F.). Gerichtsvollzieher stellen PfÜB elektronisch zu (eBO). |
| dauerhaft | § 840 ZPO Drittschuldnererklärung kann zusätzlich per Post erfolgen (Erleichterung für Banken). |

Rechtsquellen: BT-Drs. 21/4815, Bundestagsbeschluss 19.3.2026, Verkündung im BGBl bei Skill-Erstellung noch offen – `zv-elektronische-zustellung-2027` aktualisiert das Datum bei späterer Recherche.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
PFÜB BANK [Mandant] gegen [Schuldner], Az [Gericht]

Titel: [Art, Datum, Aussteller]
Forderung: EUR Haupt + EUR Zinsen + EUR Kosten = EUR gesamt
Drittschuldner: [Bank], BIC [...]
Gepfändet: gesamtes Guthaben + künftige Eingänge / nur Habensaldo / ...
Antragsweg: Papier / beA / ab 1.10.2026 XML nach § 829 Abs. 5 ZPO n.F.
Zustellung Drittsch.: GV Papier / eBO / ab 1.10.2027 Pflicht elektronisch
P-Konto-Hinweis: [ja / nein – Schuldner kann § 850k beantragen]
Moratorium § 833a: [4 Wochen – Auszahlung frühestens am DD.MM.JJJJ]

NÄCHSTER SCHRITT: Drittschuldnererklärung in 2 Wochen abwarten
WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Niemals Pfändung der IBAN als Forderung – Drittschuldner ist die Bank.
- Niemals den Sockelbetrag P-Konto unter den aktuellen Wert legen.
- Niemals vor Ablauf des Moratoriums § 833a ZPO Auszahlung verlangen.
- Bei Pfändungsversuch trotz bekannter Insolvenz: STOPP § 89 InsO.
- Ab 1.10.2027 elektronische Zustellung dokumentieren – Papier nur noch als Ausnahme.

## Querverweise

- `zv-titel-klausel-zustellung` – Vorprüfung
- `zv-kontensuche-drittschuldner` – wenn Bank unbekannt
- `zv-pfaendungstabelle-2025` – Freibeträge bei Lohnzufluss
- `zv-elektronische-zustellung-2027` – operative Umsetzung ZVollstrDigitG
- `zv-abwehr-schuldner` – Schuldnersicht
