---
name: fz-bemessungsgrundlage-2026
description: "Bemessungsgrundlage Forschungszulage ab 2026 belastbar berechnen: eigene FuE-Personalkosten, Eigenleistung 100 Euro je Stunde, Auftragsforschung 70 Prozent EU/EWR, AfA für Wirtschaftsgüter, 20-Prozent-Gemeinkostenpauschale, 12-Mio-Cap, KMU-Erhöhung. Mit Personalkostenformel, Stundenaufzeichnungsstruktur und Pitfalls zum Gesellschafter-Geschäftsführer."
---

# Bemessungsgrundlage 2026

## Worum geht es

Die Höhe der Forschungszulage hängt nicht von der BSFZ ab, sondern allein von den ansatzfähigen Aufwendungen und dem Höchstbetrag der Bemessungsgrundlage (BMG). Dieser Skill liefert die Berechnungslogik, die Personalkostenformel, die Behandlung von Auftragsforschung und Eigenleistung sowie typische Pitfalls.

Stand 2026 — alle Zahlen vom Antragsteller mit aktueller Gesetzesfassung und BMF-Verwaltungsanweisungen abzugleichen.

## Wann brauchen Sie diesen Skill

- Vor dem Finanzamt-Antrag, zur belastbaren Berechnung.
- Bei Sanity-Check der ersten Förderhöhenschätzung.
- Bei der Trennung Eigenforschung / Auftragsforschung.
- Wenn Gesellschafter-Geschäftsführer mitarbeitet (Stolperfalle).
- Bei Mehrjahresvorhaben für die jährliche Aufteilung.

## Sachrahmen — BMG-Komponenten und Caps

| Komponente | Ansatz | Maximum/Bedingung |
| --- | --- | --- |
| Eigene FuE-Personalkosten | Bruttolohn + Arbeitgeberanteil zur Sozialversicherung + Altersvorsorge | nur FuE-Anteil je Mitarbeiter |
| Eigenleistung Einzelunternehmer/persönlich tätiger Gesellschafter | ab 2026 pauschal 100 Euro je Arbeitsstunde | max. 40 Stunden je Woche |
| Auftragsforschung | 70 Prozent der Kosten | nur EU/EWR oder Wissenschaftseinrichtung; klare Leistungsbeschreibung |
| Wirtschaftsgüter | AfA, soweit dem FuE-Vorhaben zuordenbar | bewegliche abnutzbare Wirtschaftsgüter des Anlagevermögens |
| Gemein- und Betriebskosten | pauschal 20 Prozent der übrigen förderfähigen Aufwendungen | nur für Vorhaben mit Beginn nach 31.12.2025 |

**BMG-Höchstbetrag:** ab 01.01.2026 12 Mio. Euro pro Wirtschaftsjahr (verbundene Unternehmen ggf. gemeinsam — vom Antragsteller live zu prüfen).

**Fördersatz:** 25 Prozent; KMU-Erhöhung um 10 Prozentpunkte möglich (Antragstellervoraussetzungen prüfen).

## Praxisleitfaden — Personalkostenformel und Pitfalls

### Personalkostenformel

Förderfähige Personalkosten je Mitarbeiter und Wirtschaftsjahr:

```
PK_je_MA = (Bruttolohn + Arbeitgeber-SV + Altersvorsorge) × FuE-Anteil
```

FuE-Anteil ist der dokumentierte Zeitanteil aus der Stundenaufzeichnung. Pauschale Annahmen ("Herr X arbeitet zu 60 Prozent in der FuE") halten der Außenprüfung nicht stand.

### Beispiel Brutto-TV-L 13 (rein illustrativ; Werte vom Antragsteller mit aktueller Lohnabrechnung zu ersetzen)

- Bruttojahreslohn: 65.000 Euro
- Arbeitgeber-SV ca. 13.000 Euro
- Altersvorsorge ca. 4.500 Euro
- Personalvollkosten 82.500 Euro
- Dokumentierter FuE-Anteil 70 Prozent
- Förderfähig: 82.500 × 0.70 = 57.750 Euro
- Bei 25 Prozent Fördersatz: Zulage 14.437 Euro je Mitarbeiter
- Bei KMU-Erhöhung 35 Prozent: 20.212 Euro

### Stundenaufzeichnung — die Pflichtspalten

| Datum | Person | Vorhaben/AP | Stunden | Tätigkeit (FuE-konkret) | Kürzel Auftrag/Eigen |
| --- | --- | --- | --- | --- | --- |
| 12.03.2026 | M. Müller | V-1 / AP-2 | 6.5 | Aufbau Messreihe Variante A, Kalibrierung | E |
| 12.03.2026 | M. Müller | Service | 1.5 | Wartung Bestandsanlage | N |

- `E` = Eigenforschung, `A` = Auftragsforschung, `N` = nicht FuE.
- Schon dieses Detail genügt vielen Außenprüfern, weil es Konsistenz zur Projektakte zeigt.

### Eigenleistung Einzelunternehmer / persönlich tätiger Gesellschafter

- Pauschale 100 Euro je Stunde, max. 40 Stunden je Woche, ab 2026 (vom Antragsteller mit aktueller Fassung zu prüfen).
- **Pitfall Gesellschafter-Geschäftsführer:** Wer als GmbH-Gesellschafter-Geschäftsführer ein Gehalt bezieht, fällt nicht automatisch in die Eigenleistung. Die Personalkosten werden über die Lohnabrechnung berücksichtigt. Doppelansatz vermeiden.
- **Pitfall Einzelunternehmer:** Eigenleistung ist die einzige Möglichkeit, weil keine Lohnabrechnung existiert.

### Auftragsforschung — die 70-Prozent-Regel

- Förderfähig nur 70 Prozent der Kosten.
- Auftragnehmer muss in EU/EWR ansässig sein oder Wissenschaftseinrichtung.
- **Klare Leistungsabgrenzung im Vertrag.** Wer was wann mit welchem Ziel.
- Subunternehmer des Auftragnehmers werden mitgeprüft.
- Verbundene Unternehmen sind kritisch — die BSFZ und das Finanzamt prüfen genau, ob es sich nicht doch um eigene FuE im Konzern handelt.

### Wirtschaftsgüter / AfA

- Nur bewegliche, abnutzbare Wirtschaftsgüter des Anlagevermögens.
- Anteilige AfA, soweit dem FuE-Vorhaben zugeordnet.
- Keine Grundstücke, keine Software-Lizenzen mit Sonderregeln (Einzelfall prüfen).

### 20-Prozent-Gemeinkostenpauschale

- Für Vorhaben mit Beginn nach 31.12.2025.
- 20 Prozent der übrigen förderfähigen Aufwendungen (eigene Personalkosten + Eigenleistung + 70-Prozent-Auftrag + AfA).
- Keine Belegpflicht für die Pauschale selbst — die Pauschale ersetzt die Einzelbelegnahme der Gemeinkosten.

## Trade-off-Matrix

| Trade-off | Pfad A | Pfad B | Empfehlung |
| --- | --- | --- | --- |
| Eigenforschung vs. Auftragsforschung | 100 Prozent BMG | 70 Prozent BMG | Eigen bevorzugen, wenn Personal vorhanden |
| Gesellschafter Eigenleistung vs. Lohn | 100 Euro/Std., 40-Stunden-Cap | reguläre Personalkosten | Lohn meist günstiger ab ca. 30 Euro/Std. Vollkosten |
| Vollverteilung vs. konservativ | maximal anteilig | nur dokumentierte Stunden | konservativ; Außenprüfung honoriert das |
| Sammel-AP vs. detaillierte AP | weniger Verwaltung | bessere Nachvollziehbarkeit | detaillierte AP für Außenprüfung |

## Schritt für Schritt

1. Wirtschaftsjahr und Vorhaben festlegen.
2. Pro Mitarbeiter Lohnkosten + SV + Altersvorsorge ermitteln.
3. FuE-Anteil aus Stundenaufzeichnung ermitteln (Stundenzahl FuE / Stundenzahl gesamt).
4. Auftragsforschungskosten aus Rechnungen sammeln, mit 70 Prozent ansetzen.
5. Eigenleistung Einzelunternehmer / persönlich tätiger Gesellschafter mit 100 Euro × dokumentierte Stunden (max. 40/Woche).
6. AfA für Wirtschaftsgüter anteilig zuordnen.
7. Zwischensumme bilden.
8. 20-Prozent-Gemeinkostenpauschale auf die Zwischensumme aufschlagen (sofern Vorhabensbeginn nach 31.12.2025).
9. BMG-Cap prüfen (12 Mio. Euro/Jahr).
10. Fördersatz anwenden (25 Prozent oder 35 Prozent KMU).
11. Drei Szenarien dokumentieren: konservativ / realistisch / maximal.

## Mustertexte / Vorlagen

**Berechnungstabelle (Vorlage):**

| Komponente | Brutto | Faktor | Förderfähig |
| --- | --- | --- | --- |
| Personalkosten Mitarbeiter A | 82.500 Euro | 70 Prozent | 57.750 Euro |
| Personalkosten Mitarbeiter B | 75.000 Euro | 50 Prozent | 37.500 Euro |
| Eigenleistung Gesellschafter | 100 Euro × 800 Std. | 100 Prozent | 80.000 Euro |
| Auftragsforschung Institut X | 120.000 Euro | 70 Prozent | 84.000 Euro |
| AfA Maschine M-12 | 40.000 Euro | 60 Prozent | 24.000 Euro |
| Zwischensumme | | | 283.250 Euro |
| 20 Prozent Pauschale | | | 56.650 Euro |
| Bemessungsgrundlage | | | 339.900 Euro |
| Forschungszulage 25 Prozent | | | 84.975 Euro |
| Forschungszulage 35 Prozent (KMU) | | | 118.965 Euro |

**Anteilssatz-Plausibilität:** Wenn ein Mitarbeiter zu 90 Prozent in FuE arbeitet, muss in der Stundenaufzeichnung diese Quote nachweisbar sein. Das Finanzamt vergleicht Lohnkonto, Tätigkeitsbeschreibung und Stundenaufzeichnung.

## Typische Fehler

- Vollkosten ohne Stundennachweis hochgerechnet.
- Auftragsforschung mit 100 Prozent statt 70 Prozent angesetzt.
- Gesellschafter-Geschäftsführer doppelt (Lohn + Eigenleistung).
- Auftragsforschung außerhalb EU/EWR mit angesetzt.
- 20-Prozent-Pauschale auf nicht-zulässige Posten angewendet.
- 12-Mio-Cap übersehen bei verbundenen Unternehmen.

## Output

- Berechnungstabelle pro Wirtschaftsjahr.
- Beleganforderungsliste (Lohnkonten, Verträge, Rechnungen, AfA-Plan).
- Sensitivitätsanalyse konservativ / realistisch / maximal.
- Hinweis auf KMU-Voraussetzungen und Erhöhungs-Antrag (separat zu prüfen).

## Querverweise

- `fz-finanzamt-festsetzung-auszahlung` für die Antragstellung beim Finanzamt.
- `fz-dokumentationspaket-betriebspruefung` für die Belegfähigkeit.
- `fz-kumulierung-beihilfen-agvo` für AGVO-Höchstintensität.
- `fz-roadmap-mehrjahresantrag` für die Aufteilung über Wirtschaftsjahre.

## Quellen Stand 05/2026

- FZulG, insbesondere §§ 3, 4, 5 (vom Antragsteller mit konsolidierter Fassung zu prüfen).
- Wachstumschancengesetz, Auftragsforschungsregelung 70 Prozent.
- Steuerliches Investitionssofortprogramm 2025/2026: https://www.bescheinigung-forschungszulage.de/steuerliches-investitionssofortprogramm
- `references/forschungszulage-quellen-und-zahlen.md`.
