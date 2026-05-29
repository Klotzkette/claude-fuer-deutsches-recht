---
name: tenor-bauen-zivil
description: "Tenor eines Zivilurteils konstruieren: Richter muss Hauptsache-Entscheidung, Kosten und Vollstreckbarkeit klar tenorieren. Normen: §§ 91 ff. ZPO (Kosten), §§ 708-720a ZPO (vorlaeufige Vollstreckbarkeit), § 511 ZPO (Berufungszulassung), Bestimmtheitsgebot. Prüfraster: Zahlungsantrag mit Zinsen ab, Kostenquote, vorlaeufige Vollstreckbarkeit mit/ohne Sicherheitsleistung, Streitwertfestsetzung, Berufungszulassung. Output Tenor-Entwurf vollständig und vollstreckbar. Abgrenzung: Entscheidungsgründe siehe entscheidungsgründe-zivil-schreiben; Kostenentscheidung detail siehe kostenentscheidung-bauen."
---

# Tenor bauen Zivilurteil

Der Tenor ist das Herzstück des Urteils. Er muss vollstreckbar sein.


## Triage zu Beginn

1. Welche Anträge wurden gestellt — Hauptantrag, Hilfsantrag, Widerklage?
2. Ist der Kläger voll, teilweise oder gar nicht erfolgreich?
3. Welcher Zinssatz gilt — 5 Prozentpunkte über Basiszinssatz (§ 288 Abs. 1 BGB) oder 9 Prozentpunkte (§ 288 Abs. 2 BGB, B2B)?
4. Ist vorläufige Vollstreckbarkeit mit oder ohne Sicherheitsleistung anzuordnen (§ 708 Nr. 11 oder § 709 ZPO)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 253 Abs. 2 Nr. 2 ZPO — Bestimmtheitsgebot für den Antrag (gilt spiegelbildlich für Tenor)
- § 288 Abs. 1 BGB — Verzugszinssatz (5 Prozentpunkte über Basiszinssatz)
- § 288 Abs. 2 BGB — Verzugszinssatz im B2B-Bereich (9 Prozentpunkte über Basiszinssatz)
- § 291 BGB — Rechtshängigkeitszinsen (ab Klageerhebung)
- § 708 Nr. 11 ZPO — Vollstreckbarkeit ohne Sicherheit bis 1.500 EUR
- § 709 ZPO — Vollstreckbarkeit gegen Sicherheitsleistung von 110 Prozent
- § 713 ZPO — Vollstreckbarkeit ohne Sicherheit bei fehlendem Rechtsmittel

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-für-Schritt-Workflow

1. **Hauptsacheantrag prüfen:** Zahlungsbetrag, Zinssatz, Zinsbeginn — konkret und vollstreckbar formulieren.
2. **Hilfsanträge/Widerklage:** Reihenfolge wie im Klageantrag; Hilfsantrag mit "hilfsweise:" kennzeichnen.
3. **Kostenentscheidung:** § 91 ZPO (voller Sieg) oder § 92 ZPO (Quotelung).
4. **Vorläufige Vollstreckbarkeit:** Passende Norm wählen (§ 708, 709 oder 713 ZPO).
5. **Streitwertbeschluss:** Im Tenor oder separat (§ 63 GKG).

## Output-Template

**Adressat:** Urteil → Tenor — Tonfall: formal-amtlich

```
## Tenor

1. Die Beklagte wird verurteilt, an den Kläger [BETRAG] EUR nebst Zinsen in Höhe von
   fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem [DATUM] zu zahlen.
   [Im Übrigen wird die Klage abgewiesen.]

2. Die [Beklagte / Kosten werden gequotelt: Kläger X von Hundert, Beklagte Y von Hundert]
   trägt die Kosten des Rechtsstreits.

3. Das Urteil ist vorläufig vollstreckbar [gegen Sicherheitsleistung in Höhe von
   einhundertzehn Prozent des jeweils zu vollstreckenden Betrages].

4. Der Streitwert wird auf [BETRAG] EUR festgesetzt.
```

## Aufbau

1. **Hauptsache** (Verurteilung / Klageabweisung)
   - bezifferter Zahlungsantrag mit Zinsen "ab" Datum / "seit" Datum
   - bei Mehrforderungen: Reihenfolge wie im Antrag, mit Hilfsanträgen kenntlich machen
2. **Kosten** (Paragraf 91 ff ZPO)
   - bei vollem Obsiegen: "Der Beklagte traegt die Kosten des Rechtsstreits."
   - bei teilweisem Obsiegen: Quote nach Paragraf 92 ZPO
   - bei mehreren Beklagten: Paragraf 100 ZPO
3. **Vorläufige Vollstreckbarkeit** (Paragraf 708 ff ZPO)
   - Standardformel: "Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von einhundertzehn Prozent des jeweils zu vollstreckenden Betrages."
   - Bei Beschwer unter 600 EUR: Paragraf 713 ZPO - ohne Sicherheit
   - Bei Versäumnisurteil: Paragraf 708 Nr. 2 ZPO
4. **Streitwert** (gesonderter Beschluss oder im Tenor)
5. **Berufungszulassung** (Paragraf 511 Abs. 4 ZPO bei AG-Urteilen mit Beschwer unter 600 EUR)

## Bestimmtheitsgebot

Der Tenor muss aus sich heraus vollstreckbar sein. Keine Bezugnahmen auf den Tatbestand.

## Beispiele

- "Die Beklagte wird verurteilt, an den Kläger ein Komma fünffünfsiebenzig Euro (genauer: 1577 EUR oder 1577.00 EUR) nebst Zinsen in Höhe von fünf Prozentpunkten über dem jeweiligen Basiszinssatz seit dem 15. Januar 2026 zu zahlen."
- "Die Klage wird abgewiesen."
- "Die Kosten des Rechtsstreits traegt die Beklagte."
- "Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von einhundertzehn Prozent des jeweils zu vollstreckenden Betrages."
- "Der Streitwert wird auf 1577 Euro festgesetzt."

Im Repository werden Geldbetraege im Fliesstext mit Punkt geschrieben (Repo-Konvention).

---
<!-- AUDIT 27.05.2026: BGH VII ZR 213/10 (NJW 2011, 2885) auf dejure.org nicht auffindbar (NOT_FOUND) — Eintrag ersatzlos geloescht. Uebrige Rechtsprechungseintraege wurden nicht geprueft. -->
