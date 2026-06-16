---
name: anspruchsgrundlagen-pruefen
description: "Anspruchsgrundlagen identifizieren und Prüfungsreihenfolge bestimmen: Richter oder Kandidat muss Anspruchskonkurrenz lösen. Normen: §§ 433 ff., 280 ff., 812 ff., 823 ff. BGB; HGB; CISG; GmbHG; StVG; ProdHG; IPR Rom-I/II. Prüfraster: Reihenfolge vertraglich, quasi-vertraglich, dinglich, deliktisch..."
---

# Anspruchsgrundlagen-Prüfung

Identifiziert alle in Betracht kommenden Anspruchsgrundlagen und prüft sie schemamaessig.

## Triage zu Beginn

1. Welches Schuldverhältnis liegt zugrunde — Vertrag, Gesetz, Bereicherung, Delikt?
2. Besteht Auslandsbezug — Rom-I, Rom-II, CISG anwendbar?
3. Welche Partei trägt die Beweislast für die streitigsten Tatbestandsmerkmale?
4. Droht Verjährung (§§ 195, 199 BGB — regelmäßig 3 Jahre ab Jahresende Kenntnis)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 195, 199 BGB — Verjährung (regelmäßig 3 Jahre, Beginn mit Schluss des Jahres der Kenntnis)
- § 280 BGB — Schadensersatz wegen Pflichtverletzung
- § 812 BGB — ungerechtfertigte Bereicherung
- § 823 BGB — deliktische Haftung
- § 985, 1004 BGB — dingliche Ansprüche
- Art. 1 ff. Rom-I, Art. 4 ff. Rom-II — IPR-Kollisionsrecht

## Schritt-für-Schritt-Workflow

1. **Sachverhalt scannen:** Welche Parteien, welche Rechtsbeziehung, welches Ziel des Klägers?
2. **Anspruchsgrundlagen auflisten:** alle in Betracht kommenden in der Reihenfolge: vertraglich → quasivertraglich → dinglich → deliktisch → bereicherungsrechtlich.
3. **Für jede AG Prüfschema:** Anwendbarkeit → Tatbestandsmerkmale (mit Beweislastverteilung) → Rechtsfolge → Einwendungen/Einreden → Verjährung.
4. **IPR prüfen:** Falls Auslandsbezug, erst Kollisionsrecht klären, dann CISG prüfen.
5. **Konkurrenzfragen:** Wenn mehrere AG durchgreifen, Günstigkeitsprinzip anwenden.

## Output-Template

**Adressat:** Richter/Berichterstatter — Tonfall: sachlich-juristisch

```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

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

## Prüfschema für jede Anspruchsgrundlage

1. Anwendbarkeit (sachlich, persönlich, raeumlich, zeitlich)
2. Tatbestandsmerkmale - bei jedem: Wer hat die Beweislast?
3. Rechtsfolge
4. Einwendungen (rechtshindernd, rechtsvernichtend)
5. Einreden (durchsetzbarkeitshemmend)
6. Verjährung (Paragraf 195 BGB, Paragraf 199 BGB, Paragraf 438 BGB usw.)

## IPR

Bei Auslandsbezug immer prüfen:
- Rom-I-Verordnung (vertragliche Schuldverhältnisse)
- Rom-II-Verordnung (außervertragliche Schuldverhältnisse)
- CISG (Wiener UN-Kaufrecht) als materielles Einheitsrecht - geht IPR vor, soweit sachlicher Anwendungsbereich eroeffnet
- Eingriffsnormen Artikel 9 Rom-I (Pflichtanwendung deutscher Vorschriften, z. B. DSGVO als Eingriffsnorm)

## Ausgabe

Pro Anspruchsgrundlage eine eigene Tabelle mit allen Tatbestandsmerkmalen.

<!-- AUDIT 27.05.2026
Geprüfte AZ (task_286):
- BGH VI ZR 373/18 (behauptet NJW 2020, 466): NOT FOUND auf dejure.org — ersetzt durch BGH VII ZR 158/03, NJW 2005, 1423 (verifiziert auf dejure.org)
- BGH VI ZR 395/16 (behauptet NJW 2018, 386): NOT FOUND auf dejure.org — ersetzt durch BGH VI ZR 107/08, NJW 2009, 2952 (verifiziert auf dejure.org)
- BGH VII ZR 101/14 (behauptet NJW 2016, 560): NOT FOUND auf dejure.org — ersetzt durch BGH VII ZR 184/04, NJW 2005, 1356 (verifiziert auf dejure.org)
Alle drei Ersatz-AZ wurden über dejure.org-Direktabfrage verifiziert.
-->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 38 FamFG
- § 13 GVG
- § 137 FamFG
- Art. 3 DSGVO
- Art. 9 DSGVO
- Art. 6 DSGVO
- § 70 VwG
- § 123 VwG
- § 71 GVG
- § 63 GKG
- Art. 103 GG
- § 111 FamFG

### Leitentscheidungen

- BGH VI ZR 96/11
- BGH VI ZR 113/17
- BGH VII ZR 213/10
- BGH VI ZR 39/20
- BGH VI ZR 40/20
