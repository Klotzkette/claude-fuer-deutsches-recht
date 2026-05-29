---
name: gesellschaftsgruender-share-classes-a-b-c
description: "Anteilsklassen A, B, C in GmbH oder AG gestalten: unterschiedliche Gewinn-, Stimm- und Liquidationsrechte. Normen: §§ 29 47 GmbHG, §§ 11 12 AktG. Prüfraster: Satzungsgestaltung, steuerliche Wirkung, Investorenerwartungen. Output: Satzungsklauseln Anteilsklassen. Abgrenzung: nicht Golden-Share-Einzelvetorecht."
---

# Anteilsklassen A / B / C / Common

## Triage — kläre vor der Klassenstruktur

1. Liegt bereits ein Term Sheet oder LOI eines Investors vor — und fordert der Investor Vorzugsklassen?
2. Sollen Gründer vor Investor-Verwässerung geschützt werden (dann: Super-Voting Common)?
3. Ist ein ESOP-/VSOP-Pool geplant, der eine eigene Klasse benötigt?
4. Besteht bei der aktuellen Gesellschafterstruktur bereits ein Klassenkonflikt-Risiko (z.B. 50/50 ohne Stichentscheid)?
5. Sind bilinguale Klauselversionen (Deutsch/Englisch) für internationalen Investor erforderlich?

## Zentrale Normen

- **§ 45 GmbHG** — Rechte der Gesellschafter; Abweichung von Satzungsstandards durch Satzung möglich.
- **§ 47 GmbHG** — Stimmrecht: 1 EUR Stammkapital = 1 Stimme Standard; Abweichungen in Satzung zulässig.
- **§ 55 Abs. 2 GmbHG** — Bezugsrecht bei Kapitalerhöhung; Ausschluss möglich bei sachlicher Rechtfertigung.
- **§ 53 Abs. 2 GmbHG** — Satzungsänderung: 75-%-Mehrheit; Einführung von Klassen erfordert Satzungsänderung.
- **§ 14 GmbHG** — Grundrechte der Gesellschafter: Gewinnanteil, Stimmrecht, Auskunft — können in Klassen differenziert werden.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Klassen-Übersichtstabelle

| Klasse | Typischer Inhaber | Stimmrecht | Liquidation Preference | Anti-Dilution | Veto-Rechte |
|---|---|---|---|---|---|
| Common | Gründer / Management | 1:1 (oder Super-Voting) | — | — | — |
| Class A (Series A) | Erster institutioneller Investor | 1:1 oder 1:1,2 | 1x non-participating | Weighted Avg. broad | Ja |
| Class B (Series B) | Zweiter Investor | 1:1 | 1x-1,5x non-participating | Weighted Avg. broad | Ja |
| Class C+ | Spätere Runden | 1:1 | Pari passu oder 1x | Weighted Avg. broad | Ja |
| ESOP Common | Mitarbeiter (Pool) | — oder 1:1 | — | — | — |

## Typische Klauseln

### Liquidation Preference (1x non-participating)

```
§ [X] Liquidation Preference

(1) Im Fall der Auflösung der Gesellschaft, eines Unternehmensverkaufs
(Share Deal oder Asset Deal) oder einer anderen Liquidationsmassnahme
erhalten die Inhaber von Anteilen der Klasse A (Class A) vor Verteilung
an die Inhaber von Common-Anteilen einen Betrag in Höhe des jeweils
geleisteten Ausgabepreises ihrer Class-A-Anteile (Liquidation Preference).

(2) Nach Auszahlung der Liquidation Preference nach Absatz 1 nehmen
die Inhaber der Class-A-Anteile nicht weiter am Resterlös teil
(non-participating).

(3) Class-A-Inhaber koennen anstelle der Liquidation Preference waehlen,
an der Verteilung anteilig nach Nominalanteil teilzunehmen, wenn dies fuer
sie rechnerisch vorteilhafter ist.
```

### Anti-Dilution (Weighted Average broad-based)

```
§ [Y] Anti-Dilution-Schutz

Bei einer Ausgabe neuer Anteile zu einem Preis pro Anteil (Issue Price),
der unter dem Ausgabepreis der Class-A-Anteile liegt (Down Round), wird
der Ausgabepreis der Class-A-Anteile angepasst auf Basis der folgenden
gewichteten Durchschnittsformel (Weighted Average, broad-based):

CP2 = CP1 × (A + B) / (A + C)

CP1 = bisheriger Class-A-Ausgabepreis
CP2 = angepasster Class-A-Ausgabepreis
A   = Anzahl ausstehender Anteile vor Down-Round-Ausgabe
B   = Gegenwert der neuen Anteile zum bisherigen CP1 in EUR
C   = Anzahl tatsaechlich ausgegebener neuer Anteile

Die Anpassung erfolgt durch Ausgabe zusaetzlicher Class-A-Anteile oder
durch Aendrung des Ausgabepreises fuer ausstehende Class-A-Anteile.
```

## Schritt-für-Schritt-Workflow

1. **Triage** — 5 Triage-Fragen beantworten; Investor-Anforderungen klären.
2. **Klassensystem entwerfen** — Common, Class A (B, C) und ESOP-Pool definieren.
3. **Stimmrecht** — Super-Voting für Gründer? Mehrstimmrecht für bestimmte GV-Beschlüsse?
4. **Liquidation Preference** — 1x non-participating Standard; participating nur auf expliziten Investor-Wunsch.
5. **Anti-Dilution** — Weighted Average broad-based Standard; Full Ratchet nur bei Ausnahme-Investoren.
6. **Vetorechtskatalog** — welche Beschlüsse erfordern Zustimmung des Class-A-Investors?
7. **Satzungsklauseln entwerfen** — auf Basis der Muster oben; bilingual (D/E) bei internationalem Investor.
8. **Satzungsänderung** — Notar-Termin; 75-%-Mehrheit; HR-Anmeldung.

## Output-Template Klassenstruktur-Übersicht

**Adressat:** Investor / Gründer intern — Tonfall sachlich-präzise
```
KLASSENSTRUKTUR [FIRMENNAME] GMBH
Stand: [Datum]
Version: [Nr.]

CAP TABLE MIT KLASSEN
| Gesellschafter | Klasse | Anteile | % | Ausgabepreis | Liq. Pref. | Anti-Dil. | Veto |
|---------------|-------|---------|---|-------------|-----------|----------|------|
| [Gründer 1]   | Common | [Nr.]  |[%]| [EUR]       | —         | —         | — |
| [Gründer 2]   | Common | [Nr.]  |[%]| [EUR]       | —         | —         | — |
| [Investor A]  | Class A | [Nr.] |[%]| [EUR]       | 1x NP     | WA broad  | Ja |
| ESOP Pool     | Common | [Nr.]  |[%]| reserviert  | —         | —         | — |

VETORECHTE CLASS A (Investor)
[ ] Kapitalerhöhung > [EUR]
[ ] Unternehmensverkauf / Liquidation
[ ] Änderung der Investorenrechte
[ ] Ausgabe neuer Vorzugsanteile
[ ] Dividenden-Beschluss
```

## Rote Schwellen

- Bezugsrechtsausschluss für neue Klasse ohne sachliche Rechtfertigung → anfechtbar (BGH Kali+Salz).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Klassensystem ohne Satzungsgrundlage (nur in SHA) → keine dingliche Wirkung; schuldrechtlich nur.
- Full-Ratchet-Anti-Dilution ohne explizite Zustimmung aller Gründer → Verwässerungsschutz kann ruinös wirken; sorgfältig verhandeln.

## Quellen und Vertiefung

- §§ 14, 45, 47, 53, 55 GmbHG (Gesellschafterrechte, Stimmrecht, Satzungsänderung, Kapitalerhöhung)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/Seibt, GmbHG, § 47 Rn. 30-50

## Übergabe an andere Skills

- `gesellschaftsgruender-gesellschaftervereinbarung` — Liquidation Preference, Anti-Dilution im SHA
- `gesellschaftsgruender-genehmigtes-kapital` — Ausgabe neuer Klassen aus genehmigtem Kapital
- `gesellschaftsgruender-kapitalerhoehung-bezugsrecht` — ordentliche KE mit Bezugsrechtsausschluss
- `gesellschaftsgruender-klauselkatalog-bilingual` — Klauseln in Deutsch und Englisch
