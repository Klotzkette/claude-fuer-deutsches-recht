---
name: anspruchsgrundlagen-pruefen
description: "Anspruchsgrundlagen identifizieren und Pruefungsreihenfolge bestimmen: Richter oder Kandidat muss Anspruchskonkurrenz loesen. Normen: §§ 433 ff., 280 ff., 812 ff., 823 ff. BGB; HGB; CISG; GmbHG; StVG; ProdHG; IPR Rom-I/II. Pruefraster: Reihenfolge vertraglich, quasi-vertraglich, dinglich, deliktisch, bereicherungsrechtlich; Tatbestandsmerkmale, Rechtsfolge, Einwendungen, Einreden, Verjaehrung. Output Anspruchsgrundlagen-Baum mit Pruefungsschema. Abgrenzung: CISG-spezifisch siehe cisg-pruefen; IPR siehe internationales-privatrecht; Tenorierung siehe tenor-bauen-zivil."
---

# Anspruchsgrundlagen-Prüfung

Identifiziert alle in Betracht kommenden Anspruchsgrundlagen und prüft sie schemamaessig.


## Triage zu Beginn

1. Welches Schuldverhältnis liegt zugrunde — Vertrag, Gesetz, Bereicherung, Delikt?
2. Besteht Auslandsbezug — Rom-I, Rom-II, CISG anwendbar?
3. Welche Partei trägt die Beweislast für die streitigsten Tatbestandsmerkmale?
4. Droht Verjährung (§§ 195, 199 BGB — regelmäßig 3 Jahre ab Jahresende Kenntnis)?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 24.09.2019 - VI ZR 373/18, NJW 2020, 466 — Anspruchskonkurrenz zwischen § 280 BGB und § 823 BGB: jede Anspruchsgrundlage ist eigenständig zu prüfen, Einschränkungen des einen Anspruchs schlagen nicht auf den anderen durch.
- BGH, Urt. v. 26.11.2015 - VII ZR 101/14, NJW 2016, 560 — Bereicherungsrecht subsidiär bei wirksamen Vertrag; § 812 BGB setzt Fehlen eines rechtlichen Grundes voraus.
- BGH, Urt. v. 18.07.2017 - VI ZR 395/16, NJW 2018, 386 — Produkthaftung nach ProdHG und deliktische Haftung nach § 823 Abs. 1 BGB stehen selbstständig nebeneinander.
- EuGH, Urt. v. 13.07.2006 - C-295/04, NJW 2006, 2317 — Anspruchsgrundlagen aus EU-Recht (etwa Kartellschadensersatz Art. 101 AEUV) sind durch nationales Prozessrecht zu verwirklichen, dürfen aber nicht weniger günstig als rein nationale Ansprüche ausgestaltet sein.

## Zentrale Normen

- § 195, 199 BGB — Verjährung (regelmäßig 3 Jahre, Beginn mit Schluss des Jahres der Kenntnis)
- § 280 BGB — Schadensersatz wegen Pflichtverletzung
- § 812 BGB — ungerechtfertigte Bereicherung
- § 823 BGB — deliktische Haftung
- § 985, 1004 BGB — dingliche Ansprüche
- Art. 1 ff. Rom-I, Art. 4 ff. Rom-II — IPR-Kollisionsrecht

## Kommentarliteratur

- Grüneberg, BGB, 83. Aufl. 2024, Überbl. vor § 241 Rn. 1-20 (Schuldverhältnis-Typen)
- MüKo-BGB/Ernst, 9. Aufl. 2022, § 280 Rn. 1-60 (Schadensersatz Grundtatbestand)
- BeckOK-BGB/Lorenz, § 812 Rn. 1-50 (Bereicherungsrecht)

## Schritt-für-Schritt-Workflow

1. **Sachverhalt scannen:** Welche Parteien, welche Rechtsbeziehung, welches Ziel des Klägers?
2. **Anspruchsgrundlagen auflisten:** alle in Betracht kommenden in der Reihenfolge: vertraglich → quasivertraglich → dinglich → deliktisch → bereicherungsrechtlich.
3. **Für jede AG Prüfschema:** Anwendbarkeit → Tatbestandsmerkmale (mit Beweislastverteilung) → Rechtsfolge → Einwendungen/Einreden → Verjährung.
4. **IPR prüfen:** Falls Auslandsbezug, erst Kollisionsrecht klären, dann CISG prüfen.
5. **Konkurrenzfragen:** Wenn mehrere AG durchgreifen, Günstigkeitsprinzip anwenden.

## Output-Template

**Adressat:** Richter/Berichterstatter — Tonfall: sachlich-juristisch

```
## Anspruchsgrundlagen-Übersicht

| Anspruchsgrundlage | Ergebnis | Hauptproblem |
|---|---|---|
| § 433 I BGB (Kaufpreis) | (+) | — |
| § 823 I BGB (Körperverletzung) | prüfen | Kausalität str. |
| § 812 I 1 BGB (Bereicherung) | (-) | Rechtsgrund vorhanden |

### 1. § [AG] [Norm]
- **Tatbestandsmerkmale:** ...
- **Beweislast Kläger:** ...
- **Einwendungen Beklagter:** ...
- **Verjährung:** 3 Jahre ab [DATUM], läuft am [DATUM] ab.
- **Ergebnis:** Anspruch besteht / besteht nicht.
```

## Reihenfolge

1. **Vertraglich** (Paragraf 433 BGB, Paragraf 535 BGB, Paragraf 631 BGB usw. - CISG bei internationalem Warenkauf)
2. **Quasivertraglich** (Paragraf 311 II BGB - culpa in contrahendo, Paragraf 280 BGB)
3. **Dinglich** (Paragraf 985 BGB, Paragraf 1004 BGB)
4. **Deliktisch** (Paragraf 823 ff BGB, Paragraf 7 StVG, ProdHG)
5. **Bereicherungsrechtlich** (Paragraf 812 ff BGB)
6. **Familien- / erbrechtlich** soweit einschlaegig

## Pruefschema für jede Anspruchsgrundlage

1. Anwendbarkeit (sachlich, persönlich, raeumlich, zeitlich)
2. Tatbestandsmerkmale - bei jedem: Wer hat die Beweislast?
3. Rechtsfolge
4. Einwendungen (rechtshindernd, rechtsvernichtend)
5. Einreden (durchsetzbarkeitshemmend)
6. Verjaehrung (Paragraf 195 BGB, Paragraf 199 BGB, Paragraf 438 BGB usw.)

## IPR

Bei Auslandsbezug immer prüfen:
- Rom-I-Verordnung (vertragliche Schuldverhältnisse)
- Rom-II-Verordnung (außervertragliche Schuldverhältnisse)
- CISG (Wiener UN-Kaufrecht) als materielles Einheitsrecht - geht IPR vor, soweit sachlicher Anwendungsbereich eroeffnet
- Eingriffsnormen Artikel 9 Rom-I (Pflichtanwendung deutscher Vorschriften, z. B. DSGVO als Eingriffsnorm)

## Ausgabe

Pro Anspruchsgrundlage eine eigene Tabelle mit allen Tatbestandsmerkmalen.
