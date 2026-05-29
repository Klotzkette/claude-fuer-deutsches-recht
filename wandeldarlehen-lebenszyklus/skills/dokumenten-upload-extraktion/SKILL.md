---
name: dokumenten-upload-extraktion
description: "Hochgeladene Wandeldarlehens-Dokumente analysieren und Kerndaten extrahieren für Mandatsbearbeitung. BGB GmbHG Standardterminologie. Prüfraster: Vertragsparteien Darlehenshoehe Zinsen Wandlungspreisbeschreibung Trigger Laufzeit Sonderrechte. Output: strukturiertes Datenmemo mit Extraktionsergebnis. Abgrenzung: Extraktion und Triage; Detailprüfung in Spezialist-Skills."
---

# Dokumenten-Upload und Datenextraktion

## Zweck

Dieser Skill extrahiert aus hochgeladenen Transaktionsdokumenten (Term Sheet, SPA, IRA, SHA) alle für die Wandlungsrechnung relevanten Zahlen und Parameter. Phase C des Lebenszyklus.

## Eingaben

- Hochgeladene Dokumente: Term Sheet, Share Purchase Agreement (SPA), Investor Rights Agreement (IRA), Shareholders Agreement (SHA), Beteiligungsvertrag
- Gesuchte Parameter: Pre-Money, Post-Money, Investitionsvolumen, Anteilsklassen, Nennwert, Vesting, ESOP, Liquidationspräferenzen, Anti-Dilution

## Rechtlicher Rahmen

### Primärnormen
- § 15 GmbHG (Anteilsklassen und Übertragung)
- § 272 HGB (Eigenkapitalausweis nach Klassen)
- § 194 AktG analog (Wandelschuldverschreibungen und Klassen – Orientierung)

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Dokumententyp identifizieren
Term Sheet: Enthält Rahmenbedingungen (Pre-Money, Anteilsklassen, Liquidationspräferenz, Anti-Dilution, ESOP, Board-Rechte). SPA: Enthält Kaufpreis (als Post-Money oder implizit), Warranties, CP-Liste. IRA/SHA: Enthält Informationsrechte, Vetorechte, Drag-Along/Tag-Along.

### 2. Pre-Money-Bewertung extrahieren
Suche nach "pre-money valuation", "Pre-Money-Bewertung", "company valuation before investment". Umrechnung falls nur Post-Money angegeben: Pre-Money = Post-Money − Investitionsvolumen.

### 3. Investitionsvolumen extrahieren
"Investment amount", "aggregate investment", "total subscription amount". Achtung: Aufteilen nach Investorengruppen falls mehrere.

### 4. Anteilsklassen extrahieren
Bestehende und neue Anteilsklassen (Ordinary Shares, Preferred Shares A, B). Wandlungsrechte, Liquidationspräferenzen je Klasse, Dividendenpräferenzen. Einfluss auf vollverwässerte Anteile.

### 5. ESOP-Pool extrahieren
"Employee Option Pool", "Management Option Programme". Größe in Anteilen oder Prozent. Vor- oder nach-Kapitalerhöhung? (Beeinflusst vollverwässerte Basis für Wandlungspreis).

### 6. Strukturierten Extrakt ausgeben
Tabelle mit allen extrahierten Werten, Quellenangabe (Dokument, Seite, Klausel), offene Fragen markiert. Übergabe an `wandlungspreis-berechnung`.

## Beispiel-Extrakt Term Sheet

| Parameter | Wert | Quelle |
|---|---|---|
| Pre-Money-Bewertung | EUR 6000000 | Term Sheet Cl. 2.1 |
| Investitionsvolumen | EUR 1000000 | Term Sheet Cl. 2.1 |
| Anteilsklassen | Ordinary + Series A Preferred | Term Sheet Cl. 3 |
| Liquidationspräferenz Series A | 1x non-participating | Term Sheet Cl. 4 |
| ESOP-Pool | zehn Prozent (post-money) | Term Sheet Cl. 5 |
| Anti-Dilution | Broad-based weighted average | Term Sheet Cl. 6 |
| Qualifiziertes Financing nach WDV | Pre-Money ≥ EUR 4 Mio, Vol. ≥ EUR 500000 | WDV § 4.2 lit. a |
| Ist Qualified Financing? | Ja (beide Schwellen erfüllt) | Prüfung |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Term Sheet nur als Absichtserklärung | Zahlen unverbindlich | Term Sheet mit Bindungswirkung unklar | Verbindliches Term Sheet |
| ESOP-Pool post-money ohne Klarstellung | Vollverwässerte Basis falsch berechnet | Unklar ob pre/post | Eindeutig pre-money |
| Liquidationspräferenz höher als 1x | Lender-Barausschüttung bevorzugt | Participating Preferred | Non-participating 1x |
| Kein Pre-Money im Dokument | Berechnung nicht möglich | Nur Post-Money | Pre-Money explizit |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/wandlungspreis-berechnung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/cap-table-update-pre-post/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandlungspruefung-trigger-qualified-financing/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung GmbHG/HGB-Eigenkapitalausweis aktualisieren.

## Vertiefung — Relevante Normen

### Normen-Ergänzung und Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen

§ 12 HGB i.V.m. § 12 HRV (elektronische Einreichung Handelsregister) → Art. 25 eIDAS-VO (qualifizierte elektronische Signatur) → § 378 FamFG (Zurückweisung bei Formmängeln) → § 40 GmbHG (Einreichungspflicht Gesellschafterliste)
