---
name: sanierungsgewinn-verlustvortrag-sanity
description: "Sanity-Check für Verlustvorträge bei Sanierung. Prüft ob § 10d EStG, § 8c KStG-Mindestbesteuerung und § 10a Satz 1 GewStG den Sanierungsertrag bereits aufzehren. Wenn ja, ist der Antrag nach Paragraf 3a Absatz 4 EStG entbehrlich."
---

# Sanierungsgewinn — Verlustvortrag-Sanity-Check

## Fachlicher Anker

- **Normen:** § 6a, § 3a Abs. 4 EStG, § 10d EStG.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Worum geht es

Vor jedem Antrag nach § 3a Abs. 4 EStG ist zu prüfen, ob die vorhandenen Verlustvorträge den voraussichtlichen Sanierungsertrag bereits ohne Antrag aufzehren. Das ist der häufigste vergessene Pfad: Wenn KSt-Verlustvortrag, ESt-Verlustvortrag und Gewerbeverlust ausreichen, ist der Sanierungsantrag entbehrlich — und Sie ersparen sich Bindungswirkung, FA-Streit und Dokumentationsaufwand für die vier Voraussetzungen.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Wie hoch ist der voraussichtliche Sanierungsertrag (Forderungsverzicht in EUR)?
2. Wie hoch ist der Verlustvortrag zur Körperschaft- oder Einkommensteuer (§ 10d EStG)?
3. Wie hoch ist der vortragsfähige Gewerbeverlust (§ 10a Satz 1 GewStG)?
4. Welche Anteilseignerwechsel haben in der jüngeren Vergangenheit stattgefunden (§ 8c, § 8d KStG relevant)?
5. Ist die Mindestbesteuerung nach § 10d Abs. 2 EStG / § 10a Sätze 1-2 GewStG zu beachten (Sockelbetrag plus 60 %)?
6. Wirtschaftsjahr und Stichtag der Verlustfeststellung?

## Rechtlicher Rahmen

- **§ 3a Abs. 1 EStG** — Steuerbefreiung des Sanierungsertrags.
- **§ 3c Abs. 4 EStG** — Verlustreihenfolge: Verlustvorträge mindern den Sanierungsertrag, bevor die Steuerbefreiung greift. Folge: Verlustvortrag wird verbraucht.
- **§ 10d EStG** — Verlustvortrag bei der ESt.
- **§ 10a Satz 1 GewStG** — Gewerbeverlust-Vortrag.
- **§ 10a Satz 2 GewStG / § 10d Abs. 2 EStG** — Mindestbesteuerung: Sockelbetrag (1 Mio. EUR bzw. anteilig) plus 60 % des übersteigenden Gewinns.
- **§ 8c KStG, § 8d KStG** — Verlustuntergang bei Anteilseignerwechsel; Verschonungsregel.
- **§ 7b GewStG** — Gewerbesteuer-Befreiung; mit § 10a S. 1 GewStG analog gekoppelt.

## / Schritt für Schritt

| Schritt | Inhalt | Output |
|---|---|---|
| 1 | Voraussichtlichen Sanierungsertrag schätzen (Verzichtsbetrag = Buchgewinn aus Wegfall Verbindlichkeit) | EUR-Wert |
| 2 | Verlustvortrag zur KSt (§ 10d EStG) abrufen — Bescheid letzte Feststellung | EUR-Wert |
| 3 | Bei Personengesellschaft: ESt-Verlustvortrag des Gesellschafters | EUR-Wert |
| 4 | Gewerbeverlust (§ 10a S. 1 GewStG) abrufen — gesonderter Feststellungsbescheid | EUR-Wert |
| 5 | Anteilseignerwechsel >25%/>50% in letzten 5 Jahren? § 8c KStG-Verlustuntergang prüfen | Verlust ggf. weggefallen |
| 6 | § 8d KStG Verschonungsregel anwendbar? | Verlust erhalten |
| 7 | Mindestbesteuerung anwenden — Sockelbetrag 1 Mio. EUR + 60 % des übersteigenden Sanierungsertrags | maximal nutzbarer Vortrag |
| 8 | Gegenüberstellung: Sanierungsertrag vs. nutzbarer Verlustvortrag | Differenz |
| 9 | Wenn Differenz ≤ 0: kein Sanierungsantrag nötig — empfohlene Empfehlung dokumentieren | Empfehlung |
| 10 | Wenn Differenz > 0: Antrag § 3a Abs. 4 EStG für den übersteigenden Teil notwendig | Antragsgrund |

## Trade-off-Matrix

| Konstellation | Empfehlung | Begründung |
|---|---|---|
| Verlustvortrag > Sanierungsertrag, keine Mindestbesteuerung | Kein Antrag § 3a IV EStG | Antrag entbehrlich; weniger FA-Streit |
| Verlustvortrag > Sanierungsertrag, aber Mindestbesteuerung > 0 | Antrag § 3a IV EStG für Mindestbesteuerungsteil | Restbetrag steuerfrei zu stellen |
| Verlustvortrag < Sanierungsertrag | Antrag § 3a IV EStG zwingend | Sonst voll steuerpflichtig |
| § 8c KStG-Untergang droht | Antrag § 8d KStG vorrangig prüfen | Verlust retten |
| Mehrere Wirtschaftsjahre mit Verzichten | Reihenfolge der Verbrauch beachten | Strategische Aufteilung |

## Praxistipps der alten Hasen

- **§ 3c Abs. 4 EStG ist eine Falle.** Auch wenn Sie den Antrag § 3a Abs. 4 EStG nicht stellen, geht der Verlustvortrag durch den Sanierungsertrag verloren — bis er aufgebraucht ist. Vorher überlegen, ob es taktisch sinnvoll ist, Sanierungsmaßnahmen über mehrere Jahre zu verteilen.
- **Die Mindestbesteuerung trifft Sie auch bei Sanierung.** Ein vorhandener Verlustvortrag schmilzt den Sanierungsertrag, aber nicht ohne Sockelbetrag-Logik. Bei Beträgen über 1 Mio. EUR bleibt 40 % steuerpflichtig.
- **§ 8c KStG schlägt vor § 3a EStG zu.** Wenn vor der Sanierung ein Anteilseignerwechsel stattgefunden hat, ist der Verlustvortrag möglicherweise schon untergegangen. § 8d KStG-Verschonung muss aktiv beantragt werden — sonst weg.
- **Verlustfeststellungsbescheid prüfen.** Manche Mandantinnen kennen ihren Verlustvortrag nicht genau; die Feststellungsbescheide § 10d Abs. 4 EStG / § 10a S. 6 GewStG holen.
- **Gewerbeverlust separat.** § 10a S. 1 GewStG-Vortrag ist eigene Größe; nicht mit KSt-Verlustvortrag verwechseln. Gewerbesteuer-Antrag § 7b GewStG separat denken.

## Mustertexte / Berechnungsbeispiele

### Berechnungsbeispiel 1: Verlustvortrag deckt vollständig

```
Sanierungsertrag EUR 600.000
KSt-Verlustvortrag EUR 900.000
Gewerbeverlust-Vortrag EUR 700.000

Mindestbesteuerung KSt:
 Sockel 1.000.000 + 60 % (600.000 - 1.000.000) → entfaellt
 Sanierungsertrag < Sockel; voll nutzbar

► Verbrauch KSt 600.000 (Verlustvortrag verbleibt 300.000)
► Verbrauch GewSt 600.000 (Vortrag verbleibt 100.000)
► Antrag § 3a IV EStG: NICHT erforderlich
► Bindungswirkung vermieden
```

### Berechnungsbeispiel 2: Verlustvortrag deckt teilweise

```
Sanierungsertrag EUR 2.500.000
KSt-Verlustvortrag EUR 1.500.000

Mindestbesteuerung KSt:
 Sockel 1.000.000 + 60 % (2.500.000 - 1.000.000) = 1.900.000
 maximal nutzbarer Vortrag EUR 1.500.000 (limitiert durch Vortrag selbst)

 ► Sanierungsertrag 2.500.000
 ► nutzbarer Vortrag 1.500.000
 ► verbleibend steuerpflichtig 1.000.000

► Antrag § 3a IV EStG: erforderlich für 1.000.000
► Verlustvortrag wird voll verbraucht
```

### Berechnungsbeispiel 3: § 8c KStG-Falle

```
Anteilseignerwechsel 60 % im Februar Jahr X
 ► Verlustvortrag KSt geht unter (§ 8c KStG)
 ► sofern nicht § 8d KStG-Antrag in Steuererklärung Jahr X gestellt

Sanierungsforderungsverzicht im November Jahr X
 ► Sanierungsertrag voll steuerpflichtig
 ► Antrag § 3a IV EStG zwingend

Lehre: Vor Sanierung § 8d KStG-Antrag sichern.
```

## Typische Fehler

- Verlustvortrag aus Modellwissen geschätzt statt aus Bescheid abgerufen.
- Mindestbesteuerung übersehen — überraschend hohe Steuerlast trotz Verlustvortrag.
- § 8c KStG-Verlustuntergang nicht geprüft; Vortrag im Antrag falsch angesetzt.
- Gewerbeverlust mit KSt-Verlustvortrag verwechselt; § 7b GewStG-Antrag fehlt.
- Sanierungsertrag vor Verlustverbrauch in Steuererklärung nicht klar deklariert.

## Querverweise

- `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-10a-s-1-gewstg-gewerbeverlust`
- `stb-sanierungsgewinn-7b-gewstg-gewerbesteuer-parallel`
- `stb-sanierungsgewinn-fruehwarnung-monat-zwoelf-vor-plan`

## Quellen Stand 06/2026

### Normen

- § 3a Abs. 1 EStG.
- § 3a Abs. 4 EStG.
- § 3c Abs. 4 EStG.
- § 10d EStG (Verlustvortrag ESt).
- § 10d Abs. 2 EStG (Mindestbesteuerung Sockelbetrag).
- § 10a Satz 1 GewStG (Gewerbeverlust).
- § 10a Sätze 2-3 GewStG (Mindestbesteuerung GewSt).
- § 7b GewStG.
- § 8c, § 8d KStG.
- § 11 KStG (Liquidationsbesteuerung).
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.

### Rechtsprechung Mindestbesteuerung / Definitiveffekt (verifiziert)

- **FG Düsseldorf, Urt. v. 18.09.2018 — 6 K 454/15 K, DStRE 2019** — Mindestbesteuerung in Liquidation und Definitiveffekt. Revision anhängig BFH I R 36/18 (ausgesetzt wegen BVerfG 2 BvL 19/14, Vorlage durch BFH I R 59/12).
- Verfassungsrechtliche Argumentation: Verluste aus der Vergangenheit sollten in voller Höhe abzugsfähig sein — anders entstehen unzulässige Definitiveffekte (Art. 3 Abs. 1 GG).

### Verwaltungsauffassung

- **OFD Frankfurt, Verfügung v. 27.12.2018, BeckVerw 447487** — Einsprüche zur Mindestbesteuerung ruhend zu stellen.
- **OFD Frankfurt a. M., Rundverfügung v. 26.07.2021 — S 2743 A-12-St 523, BeckVerw 556782**.
- **OFD Frankfurt a. M., Rundverfügung v. 03.08.2018 — S 2743 A-12-St 525, DStR 2019, 560**.

### Querverweis Liquidations-Fachmodul

- `stb-sanierungsgewinn-stehengelassene-verbindlichkeiten` — Drei-Phasen-Analyse: bei Liquidation Wegfall der Verbindlichkeit mit Erloeschen mangels Steuersubjekt (FG Köln 13 K 3006/11), wodurch der Definitiveffekt sich nicht materialisiert.
