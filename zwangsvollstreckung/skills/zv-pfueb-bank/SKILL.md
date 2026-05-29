---
name: zv-pfueb-bank
description: "Gläubiger will Bankkonto des Schuldners pfaenden lassen. §§ 829 835 ZPO PfUeB Bankkonten. Prüfraster: Antrag Drittschuldner-Bank P-Konto-Schutz § 850k ZPO Sockelbetrag Kindergeld Erhöhungen ZVollstrDigitG XML-Antrag ab 1.10.2026 elektronische Zustellung ab 1.10.2027. Output: PfUeB-Antrag Konto fertig zum Einreichen. Abgrenzung zu zv-pfueb-arbeitsentgelt (Lohn) und zv-eu-kontenpfaendung-655-2014 (Auslands-Konto)."
---

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

Titel:                 [Art, Datum, Aussteller]
Forderung:             EUR Haupt + EUR Zinsen + EUR Kosten = EUR gesamt
Drittschuldner:        [Bank], BIC [...]
Gepfändet:             gesamtes Guthaben + künftige Eingänge / nur Habensaldo / ...
Antragsweg:            Papier / beA / ab 1.10.2026 XML nach § 829 Abs. 5 ZPO n.F.
Zustellung Drittsch.:  GV Papier / eBO / ab 1.10.2027 Pflicht elektronisch
P-Konto-Hinweis:       [ja / nein – Schuldner kann § 850k beantragen]
Moratorium § 833a:     [4 Wochen – Auszahlung frühestens am DD.MM.JJJJ]

NÄCHSTER SCHRITT:      Drittschuldnererklärung in 2 Wochen abwarten
WIEDERVORLAGE:         DD.MM.JJJJ
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
