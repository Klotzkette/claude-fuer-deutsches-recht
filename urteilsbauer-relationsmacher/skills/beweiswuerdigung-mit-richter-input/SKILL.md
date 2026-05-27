---
name: beweiswuerdigung-mit-richter-input
description: "Strukturierte Beweiswuerdigung nach § 286 ZPO schreiben: Richter hat Beweise erhoben und will Entscheidungsgruende-Abschnitt verfassen. Normen: § 286 ZPO (freie Beweiswuerdigung), § 261 ZPO (Beweislast), §§ 414 ff. ZPO (Sachverstaendige). Pruefraster: Glaubwuerdigkeit, Glaubhaftigkeit, Aussagekonstanz, Realkennzeichen, Widersprueche, Sachverstaendigen-Bewertung. Output Beweiswuerdigung-Abschnitt fuer Entscheidungsgruende. Abgrenzung: Beweisbeschluss vorher siehe beweisbeschluss-vorbereiten; Entscheidungsgruende gesamt siehe entscheidungsgruende-zivil-schreiben."
---

# Beweiswürdigung mit haendischem Richter-Input

Die Beweiswürdigung ist Kernkompetenz der Richterin oder des Richters. Sie laesst sich nicht automatisieren - aber strukturieren.


## Triage zu Beginn

1. Welche Beweismittel wurden erhoben — Zeugen, Sachverständiger, Augenschein, Urkunden?
2. Hat die Richterin/der Richter konkrete Eindrücke zur Glaubwürdigkeit der Zeugen?
3. Widersprechen sich Zeugenaussagen oder Urkunde und Aussage?
4. Ist das Sachverständigengutachten vollständig oder besteht Ergänzungsbedarf (§ 411 ZPO)?

## Aktuelle Rechtsprechung

- BGH, Urt. v. 13.09.2023 - IV ZR 228/22, NJW 2023, 3515 — Beweiswürdigung ist Sache des Tatrichters; Revisionsgericht prüft nur ob Würdigung lückenhaft, widersprüchlich oder gegen Denk- und Erfahrungssätze verstößt.
- BGH, Urt. v. 17.04.2012 - VI ZR 96/11, NJW 2012, 2194 — Aussage-gegen-Aussage: Gericht muss alle relevanten Umstände, insbesondere Konstanz, Detailreichtum und Eigeninteresse, abwägen.
- BGH, Urt. v. 12.04.2011 - VI ZR 300/09, NJW 2011, 1811 — Sachverständigengutachten ist auf Plausibilität zu überprüfen; Gericht muss Bedenken gegen das Gutachten dem Sachverständigen vorlegen (§ 411 ZPO).
- BGH, Urt. v. 29.01.2019 - VI ZR 113/17, NJW 2019, 1668 — Parteivernehmung nach § 448 ZPO nur, wenn Anbeweis für Parteivortrag bereits erbracht ist.

## Zentrale Normen

- § 286 ZPO — freie Beweiswürdigung, Vollüberzeugung
- § 313 Abs. 2 S. 2 ZPO — Bezugnahme auf Aussagen und Gutachten im Tatbestand
- § 373 ff. ZPO — Zeugenbeweis
- § 402, 411 ZPO — Sachverständiger, Ergänzungsgutachten
- § 448 ZPO — Parteivernehmung von Amts wegen

## Kommentarliteratur

- Zöller/Greger, ZPO, 35. Aufl. 2024, § 286 Rn. 1-30 (Beweiswürdigung Grundsätze)
- Thomas/Putzo, ZPO, 45. Aufl. 2024, § 286 Rn. 1-20
- MüKo-ZPO/Hauger, 6. Aufl. 2022, § 411 Rn. 1-20 (Sachverständigengutachten)

## Schritt-für-Schritt-Workflow

1. **Beweismittel auflisten:** chronologische Liste aller erhobenen Beweismittel aus dem Protokoll.
2. **Richter-Input einholen (MANUELL):** Richterin/Richter gibt strukturiert ein:
   - Glaubwürdigkeit jedes Zeugen (Eigeninteresse, persönlicher Eindruck)
   - Glaubhaftigkeit der Aussage (Konstanz, Detailreichtum, Realkennzeichen)
   - Widersprüche zu anderen Beweismitteln
3. **Würdigung formulieren:** Aus dem Input vollständige Sätze für die Entscheidungsgründe.
4. **Bezugnahme einfügen:** Verweis auf Protokoll und Gutachten nach § 313 Abs. 2 S. 2 ZPO.
5. **Feststellung zusammenfassen:** "Das Gericht hat sich davon überzeugt, dass ..."

## Output-Template

**Adressat:** Entscheidungsgründe → Abschnitt Beweiswürdigung — Tonfall: sachlich-juristisch

```
## Beweiswürdigung

Das Gericht hat die Klägerin (Parteivernehmung, Protokoll v. [DATUM]) und die Zeugen
[ZEUGE1] und [ZEUGE2] vernommen sowie das schriftliche Sachverständigengutachten
des Sachverständigen [NAME] v. [DATUM] verwertet.

Der Zeuge [ZEUGE1] hat ausgesagt, [ZUSAMMENFASSUNG]. Das Gericht hält diese Aussage
für glaubhaft. Sie war in sich konsistent, detailreich und widersprach nicht den
urkundlichen Belegen (Anlage K3). Eigeninteresse des Zeugen war nicht erkennbar.

Dem Sachverständigengutachten folgt das Gericht, soweit es [PUNKT]. Im Übrigen
hat der Sachverständige in seiner Ergänzung v. [DATUM] klargestellt, dass [PUNKT].

Das Gericht stellt fest: [FESTGESTELLTE TATSACHE].
```

## Vorgehen

1. **Schritt 1 (automatisierbar)**: Beweismittel sortieren - Zeuge / Sachverständiger / Augenschein / Urkunde / Parteivernehmung. Inhalte aus dem Sitzungsprotokoll übernehmen.
2. **Schritt 2 (haendisch)**: Die Richterin / der Richter trifft die Würdigung. Das Plugin fragt strukturiert ab:
   - **Glaubwürdigkeit des Zeugen**: persönliche Verhältnisse, Eigeninteresse, Belastungsmotivation
   - **Glaubhaftigkeit der Aussage**: Aussagekonstanz, Detailreichtum, Realkennzeichen, raumzeitliche Verknuepfungen, ungewoehnliche Detailangaben, Selbstkorrekturen, eigene Beteiligung
   - **Widersprüche** zu anderen Beweismitteln / Akten
3. **Schritt 3 (automatisierbar)**: Aus der Würdigung den Beweiswürdigungsteil der Entscheidungsgründe formulieren - in vollständigen Sätzen, mit Bezug auf die konkrete Beweisaufnahme.

## Form

Im Urteil immer:
- klare Aussage zur Beweiserhebung
- konkrete Inhaltsangabe der Aussage (kurz)
- die Würdigung mit den oben genannten Kriterien
- Ergebnis (festgestellt / nicht festgestellt)

## Bezugnahme

Auf das Sitzungsprotokoll und auf das Sachverständigengutachten ist nach Paragraf 313 II 2 ZPO konkret Bezug zu nehmen.

## Output

Strukturierte Datei `beweiswuerdigung.md` mit den Aussagen, der Würdigung und der zusammenfassenden Feststellung.
