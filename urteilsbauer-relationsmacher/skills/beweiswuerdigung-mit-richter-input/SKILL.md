---
name: beweiswuerdigung-mit-richter-input
description: "Strukturierte Beweiswürdigung nach § 286 ZPO schreiben: Richter hat Beweise erhoben und will Entscheidungsgründe-Abschnitt verfassen. Normen: § 286 ZPO (freie Beweiswürdigung), § 261 ZPO (Beweislast), §§ 414 ff. ZPO (Sachverständige). Prüfraster: Glaubwürdigkeit, Glaubhaftigkeit, Aussagekonstanz, Realkennzeichen, Widersprueche, Sachverständigen-Bewertung. Output Beweiswürdigung-Abschnitt für Entscheidungsgründe. Abgrenzung: Beweisbeschluss vorher siehe beweisbeschluss-vorbereiten; Entscheidungsgründe gesamt siehe entscheidungsgründe-zivil-schreiben."
---

# Beweiswürdigung mit haendischem Richter-Input

Die Beweiswürdigung ist Kernkompetenz der Richterin oder des Richters. Sie laesst sich nicht automatisieren - aber strukturieren.


## Triage zu Beginn

1. Welche Beweismittel wurden erhoben — Zeugen, Sachverständiger, Augenschein, Urkunden?
2. Hat die Richterin/der Richter konkrete Eindrücke zur Glaubwürdigkeit der Zeugen?
3. Widersprechen sich Zeugenaussagen oder Urkunde und Aussage?
4. Ist das Sachverständigengutachten vollständig oder besteht Ergänzungsbedarf (§ 411 ZPO)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026: BGH VI ZR 96/11 geloescht – AZ auf dejure.org nicht auffindbar (NOT_FOUND). BGH VI ZR 113/17 korrigiert – Thema war falsch angegeben (Parteivernehmung § 448 ZPO statt Beweismaß § 287 ZPO) und NJW-Fundstelle korrigiert (2019, 2092 statt 2019, 1668). -->

## Zentrale Normen

- § 286 ZPO — freie Beweiswürdigung, Vollüberzeugung
- § 313 Abs. 2 S. 2 ZPO — Bezugnahme auf Aussagen und Gutachten im Tatbestand
- § 373 ff. ZPO — Zeugenbeweis
- § 402, 411 ZPO — Sachverständiger, Ergänzungsgutachten
- § 448 ZPO — Parteivernehmung von Amts wegen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
