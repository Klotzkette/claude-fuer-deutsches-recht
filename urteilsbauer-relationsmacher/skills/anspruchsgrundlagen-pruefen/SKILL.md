---
name: anspruchsgrundlagen-pruefen
description: "Für Anspruchsgrundlagen-Prüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix."
---

# Anspruchsgrundlagen-Prüfung

Identifiziert alle in Betracht kommenden Anspruchsgrundlagen und prüft sie schemamaessig.

## Triage zu Beginn

1. Welches Schuldverhältnis liegt zugrunde — Vertrag, Gesetz, Bereicherung, Delikt?
2. Besteht Auslandsbezug — Rom-I, Rom-II, CISG anwendbar?
3. Welche Partei trägt die Beweislast für die streitigsten Tatbestandsmerkmale?
4. Droht Verjährung (§§ 195, 199 BGB — regelmäßig 3 Jahre ab Jahresende Kenntnis)?

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

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



## Quellenkontrolle

Für die Relation gelten keine universellen materiell-rechtlichen Leitentscheidungen. Zuerst Anspruchsgrundlage und Einwendungen des konkreten Streitstoffs bestimmen; pro Rechtssatz nur eine Entscheidung mit Gericht, Datum, Aktenzeichen, tragender Aussage und Quelle verwenden. Verfahrensrechtlich insbesondere Paragraf 138, Paragraf 139, Paragraf 253 Absatz 2 Nummer 2, Paragraf 286, Paragraf 296 und Paragraf 308 ZPO fallbezogen prüfen.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
