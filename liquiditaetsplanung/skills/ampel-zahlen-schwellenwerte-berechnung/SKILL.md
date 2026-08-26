---
name: ampel-zahlen-schwellenwerte-berechnung
description: "Für Ampel: Zahlen, Schwellenwerte und Berechnung: rechnet Beträge, Schwellen und Varianten; Ergebnis: Berechnungstabelle mit Annahmen und Kontrollfragen."
---

# Ampel: Zahlen, Schwellenwerte und Berechnung

## Fachkern: Ampel: Zahlen, Schwellenwerte und Berechnung
- **Normen-/Quellenanker:** InsO §§ 17, 18, 19, 15a, StaRUG-Früherkennung, IDW-S-6-/Planungslogik, 3-Wochen- und 13-Wochen-Forecast, Zahlungsstatus und Fortbestehensprognose.
- **Entscheidende Weiche:** Trenne fällige Verbindlichkeiten, liquide Mittel, harte Zahlungszusagen, Planannahmen, Quote/Lücke, Organpflicht und Dokumentationsspur.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Ampel** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Berechnungsschemata Liquiditätsstatus / -planung

### Liquiditätsstatus zum Stichtag (§ 17 InsO)
| Position | Anmerkung |
|---|---|
| Liquide Mittel (Kasse, Bank, Tagesgeld) | Saldo zum Stichtag |
| + Innerhalb 3 Wochen eingehende Forderungen | OPOS Debitoren mit Fälligkeit |
| + Frei verfügbare Kreditlinien | nur ungekündigt und nicht ausgeschöpft |
| **= Aktiva I** | „Verfügbare Mittel" |
| Fällige Verbindlichkeiten zum Stichtag | OPOS Kreditoren |
| + Innerhalb 3 Wochen fällig (Lohn, USt, KSt, SV) | streng |
| **= Passiva I** | „Fällige Verbindlichkeiten" |
| **Liquiditätslücke = P1 − A1** | wenn ≥ 10 Prozent und 3 Wochen: § 17 InsO |

### 13-Wochen-Liquidität (operativ Krisensteuerung)
- Granularität: wöchentlich.
- Cash-Inflows: Debitoren-Eingänge (Aging), Vorauszahlungen, Erstattungen.
- Cash-Outflows: Lohn/Gehalt mit Auszahlungstag, Lohnsteuer/SV-Abgaben (§ 266a StGB nicht stunden), USt-Vorauszahlung, Miete, Tilgung/Zinsen, Lieferanten nach Fälligkeit, sonstige Betriebsausgaben.
- Endbestand pro Woche: Anfang + Inflow − Outflow.

### 24-Monats-Liquiditätsplan nach Paragraf 18 Absatz 2 InsO
- Granularität: monatlich, integriert mit GuV-Forecast und Bilanzplanung.
- Sensitivität: Base/Best/Worst.

## Schwellenwerte und Ampel

- **GRÜN:** Liquiditätsdeckung > 110 Prozent in jeder Periode des 24-Monats-Horizonts; 13-Wochen-Cash-Reichweite > 6 Wochen Puffer.
- **GELB:** Liquiditätsdeckung 100–110 Prozent oder Worst-Case unter 100 Prozent — bestandsgefährdende Entwicklung nach Paragraf 1 StaRUG prüfen, Maßnahmen- und Organbericht vorbereiten.
- **ROT:**
 - Liquiditätslücke ≥ 10 Prozent über 3 Wochen → § 17 InsO Zahlungsunfähigkeit, Antragsfrist § 15a InsO.
 - 24-Monats-Plan zeigt Lücke → § 18 InsO drohende ZU, StaRUG-Tor offen.

## Berechnungs-Plausibilitäten
- Anfangsbestand Periode n+1 = Endbestand Periode n (Saldenkonsistenz).
- Working Capital (Debitoren/Kreditoren/Vorräte) realistisch zur Vergangenheit (DSO, DPO, DIO)?
- Kreditlinien-Inanspruchnahme realistisch? Kündigungsrisiko bei Krise eingerechnet?
- Steuern und SV: keine Stundungen ohne schriftliche Zusage Finanzamt / SV-Träger einplanen.

## Anti-Halluzinations-Hinweis
- 10-Prozent / 3-Wochen-Schwelle ist BGH-Linie zu § 17 InsO — keine erfundenen Az.
- Prognosezeitraum § 18 InsO: **24 Monate**; § 19 InsO Fortbestehensprognose: **12 Monate**.
