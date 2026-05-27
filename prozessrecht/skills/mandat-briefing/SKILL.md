---
name: mandat-briefing
description: "Mandantenbriefing fuer Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: §§ 373 ff. ZPO. Pruefraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument fuer Mandanten vor Termin. Abgrenzung: nicht Zeugenvorbereitung (eigener Skill)."
---

# Mandat-Briefing

## Zweck

Erzeugung eines strukturierten Tiefenbriefings zu einem einzelnen Mandat auf Basis der `mandat.md` und `verlauf.md`. Das Briefing fasst den aktuellen Verfahrensstand zusammen, identifiziert offene Handlungspunkte, prüft die nächste Frist und bewertet das Prozessrisiko neu. Einsatz vor Mandantengesprächen, GC/Justiziarssitzungen, Außenanwalts­telefonate oder vor internen Review-Terminen.

## Eingaben

- Mandat-Slug
- Optional: Fokusthema (`--frist`, `--risiko`, `--naechste-schritte`)
- Optional: Empfänger (`--mandant`, `--justiziar`, `--anwalt`) – steuert Detailgrad und Stil

## Ablauf

1. **Mandatsdaten laden:** `mandate/[slug]/mandat.md` und `mandate/[slug]/verlauf.md` einlesen.

2. **Verfahrensstand zusammenfassen:**
   - Parteien, Gericht, Aktenzeichen
   - Verfahrensstadium (Klagezustellung, Schriftsatzphase, Beweisaufnahme, Urteil, Rechtsmittel, Vollstreckung)
   - Ansprüche / Streitgegenstand (§ 264 ZPO)
   - Bisheriger Verfahrensverlauf (Chronologie der Verfahrenshandlungen)

3. **Entwicklungen seit letztem Update:**
   - Letzte Eintrag in verlauf.md identifizieren
   - Neue Schriftsätze, Gerichtsentscheidungen, Vergleichsgespräche

4. **Fristen-Check:**
   - Nächste Frist (Schriftsatzfrist, Berufungsfrist, Urteilsfrist, Vollstreckungsverjährung)
   - Risiko-Frist (in roter Zone wenn < 14 Tage)

5. **Offene Handlungspunkte:**
   - Was muss der Anwalt noch erledigen?
   - Was ist von der Gegenseite / dem Gericht ausstehend?
   - Welche Beweise fehlen noch?

6. **Risikoneueinschätzung:**
   - Änderung der Risikoeinschätzung seit letztem Intake? (BGH-Rechtsprechung, neue Sachverhalte)
   - Expositionsschätzung (untere / mittlere / obere Schadenswert-Bandbreite)
   - Vergleichspotential (§ 278 Abs. 1 ZPO: Gericht soll in jeder Lage des Verfahrens auf Vergleich hinwirken)

7. **Ausgabe:** Strukturiertes Briefing-Memo im Urteilsstil oder als Executive Summary.

## Quellen und Zitierweise

Verbindlich: `../references/zitierweise.md`.

- Greger, in: Zöller, ZPO, 35. Aufl. 2024, § 278 Rn. 1 ff. (Güteverhandlung, Vergleich: Pflicht des Gerichts zur Vergleichsförderung in jeder Lage des Verfahrens).
- BGH, Urt. v. 22.11.2023 – IV ZR 197/22, NJW 2024, 348 Rn. 12 (Änderung der Anspruchsgrundlage nach § 264 ZPO: keine Klageänderung).
- BGH, Urt. v. 05.07.2023 – VIII ZR 91/22, NJW 2023, 2893 Rn. 22 (Streitwertfestsetzung und Kostenrisiko bei Teilklagerücknahme).
- Schulze, in: BeckOK ZPO, 52. Ed. (Stand 01.03.2024), § 264 Rn. 8 ff. (Klageänderung, Streitgegenstand).

## Ausgabeformat

```
MANDAT-BRIEFING
──────────────────────────────────────
Mandat:         [Slug]
Parteien:       [Kläger] ./. [Beklagter]
Gericht / Az.:  [Gericht], Az. [JJJJ] [Aktenzeichen]
Verfahrensstufe: [z. B. Berufung – OLG Frankfurt]
Stand:          TT.MM.JJJJ
MANDATSGEHEIMNIS – § 43a Abs. 2 BRAO

──────────────────────────────────────
1. VERFAHRENSSTAND
──────────────────────────────────────
[Kurzdarstellung: Wo sind wir? Was wurde bisher eingereicht / entschieden?]

──────────────────────────────────────
2. ENTWICKLUNGEN SEIT [DATUM LETZTES UPDATE]
──────────────────────────────────────
[Neue Schriftsätze, Urteile, Korrespondenz]

──────────────────────────────────────
3. NÄCHSTE FRIST
──────────────────────────────────────
⚠️ [Frist] – [Beschreibung] – [Datum]

──────────────────────────────────────
4. OFFENE HANDLUNGSPUNKTE
──────────────────────────────────────
□ [Punkt 1]
□ [Punkt 2]

──────────────────────────────────────
5. RISIKOEINSCHÄTZUNG
──────────────────────────────────────
Expositionsschätzung: EUR [X] – EUR [Y]
Risikostufe: 🔴 hoch / 🟡 mittel / 🟢 gering
Vergleichspotential: [Einschätzung]
```

## Risiken / typische Fehler

- **Veraltete mandat.md:** Ohne regelmäßige Updates per `/mandat-update` liefert das Briefing einen falschen Stand; nach jeder Entwicklung updaten.
- **Fristversäumnis-Risiko:** Das Briefing ersetzt nicht den Fristenkalender; jede Frist muss separat in das Kanzlei-Fristbuch eingetragen werden.
- **Vertraulichkeit des Briefings:** Das Briefing enthält Mandatsgeheimnisse; Empfängerkreis sorgfältig wählen (§ 43a Abs. 2 BRAO); nicht per unverschlüsselter E-Mail versenden.
