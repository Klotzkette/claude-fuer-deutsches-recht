---
name: aktenauszug-strukturpruefung
description: "Fertig erstellten Aktenauszug auf Vollstaendigkeit pruefen: alle Bausteine vorhanden Fristen hervorgehoben neutrale Sprache. Normen §§ 128-134 253 ZPO. Pruefraster Bausteine-Vollstaendigkeit Fristen-Markierung Neutralitaets-Check Sprach-Qualitaet. Output Pruefergebnis-Bericht Lueckenliste Verbesserungshinweise. Abgrenzung zu aktenauszug-erstellen (Erstellung) und neutralitaetspruefung (Wertungs-Check)."
---

# Aktenauszug — Strukturprüfung

## Zweck

Dieser Skill prüft einen erstellten Aktenauszug auf formale Vollständigkeit aller sechs Bausteine und auf die Einhaltung der Qualitätsgrundsätze (Fristen hervorgehoben, Sprache neutral). Er ist das abschließende Qualitätsgate vor der Übergabe an den Mandatsbearbeiter.

## Triage — Kläre vor der Prüfung

1. Für welche Verfahrensart wurde der Aktenauszug erstellt? (Zivil/Arbeit/Verwaltung/Sozial/Straf)
2. Ist der Aktenauszug als intern-anwaltlicher Vermerk oder als Übergabedokument konzipiert?
3. Steht ein konkreter Termin oder eine Frist bevor, die besonders zu prüfen ist?

## Zentrale Normen

- § 128 ZPO — Muendliche Verhandlung; § 128a ZPO — Ton-/Bildübertragung
- § 139 ZPO — Materielle Prozessleitung (Hinweispflicht des Gerichts)
- § 253 ZPO — Inhalt der Klageschrift (Mindestinhalt als Vergleichsmassstab)
- § 495a ZPO — Vereinfachtes Verfahren unter 600 EUR
- §§ 355-414 ZPO — Beweisaufnahme (Zeugenbeweis, Sachverständigenbeweis, Augenschein)

## Rechtsprechung zu Vollstaendigkeit und Ordnung der Akte

- BGH, Urt. v. 17.03.2022 - IX ZR 147/20, NJW 2022, 2106 — Zur Rekonstruktion eines Sachverhalts aus unvollständiger Akte; lückenhafte Dokumentation geht zu Lasten der beweispflichtigen Partei.
- BGH, Beschl. v. 12.01.2021 - VIII ZB 73/19, NJW-RR 2021, 571 — Fristversäumnis wegen unzureichender Aktenkontrolle begründet Anwaltshaftung nach § 280 Abs. 1 i.V.m. § 675 BGB.
- BGH, Urt. v. 09.06.2020 - VI ZR 261/19, NJW 2020, 2811 — Anforderungen an die Vollständigkeit des Tatbestandes im Urteil; Aktenauszug muss tatbestandsrelevante Tatsachen vollständig abbilden.
- BVerfG, Beschl. v. 30.04.2003 - 1 PBvU 1/02, BVerfGE 107, 395 — Rechtliches Gehör (Art. 103 Abs. 1 GG) als Massstab: Gericht muss gesamten Akteninhalt kennen und berücksichtigen.

## Kommentarliteratur

- Zöller/Greger ZPO, § 139 Rn. 1 ff. (Hinweispflicht und Folgen der Verletzung)
- MüKo ZPO/Fritsche, § 253 Rn. 1 ff. (Klageschrift Mindestinhalt)
- Thomas/Putzo ZPO, § 128 Rn. 1 ff. (Muendliche Verhandlung)

## Prüfcheckliste

### Baustein 1 — Verfahrensidentifikation

- [ ] Gericht und Kammer angegeben
- [ ] Aktenzeichen angegeben
- [ ] Instanz und Verfahrensart angegeben
- [ ] Streitwert angegeben (oder als unbekannt markiert)
- [ ] Alle Parteien mit Prozessbevollmächtigten aufgeführt

### Baustein 2 — Einleitungssatz

- [ ] Ein bis zwei Sätze vorhanden
- [ ] Wer streitet mit wem worüber benannt
- [ ] Hauptnorm genannt
- [ ] Keine Wertung enthalten

### Baustein 3 — Zusammenfassung

- [ ] Acht bis zehn Sätze vorhanden
- [ ] Hintergrund dargestellt
- [ ] Aktueller Verfahrensstand benannt
- [ ] Nächste Verfahrenshandlung benannt
- [ ] Keine Wertung / Prognose enthalten

### Baustein 4 — Sachverhaltschronologie

- [ ] Chronologisch sortiert
- [ ] Datum fettgedruckt vorangestellt
- [ ] Wesentliche außerprozessuale Ereignisse vollständig
- [ ] Fundstellen angegeben
- [ ] Keine prozessualen Schritte enthalten

### Baustein 5 — Verfahrenschronologie

- [ ] Chronologisch sortiert
- [ ] Alle prozessualen Schritte erfasst
- [ ] Fristen hervorgehoben (Präfix ⚠️ FRIST)
- [ ] Fristentabelle vorhanden
- [ ] Keine außerprozessualen Ereignisse enthalten

### Baustein 6 — Tabellen

**Parteivortrag:**
- [ ] Tabelle mit zwei Spalten (Kläger / Beklagter)
- [ ] Alle wesentlichen Streitpunkte als Zeilen
- [ ] Fundstellen angegeben

**Beweismittel:**
- [ ] Alle angebotenen Beweismittel erfasst
- [ ] Beweisthema je Beweismittel angegeben
- [ ] Anlagenbezeichnung angegeben

**Rechtsargumente:**
- [ ] Anspruchsgrundlagen beider Seiten erfasst
- [ ] Einwendungen und Einreden erfasst
- [ ] Verjährungsthema behandelt (falls relevant) — §§ 195-218 BGB
- [ ] Rechtsprechung mit Aktenzeichen angegeben

## Qualitätsgrundsätze

- [ ] Neutralitätsprüfung bestanden (keine Wertungen, keine Prognosen)
- [ ] Keine verbotenen Begriffe (keine KI-Terminologie)
- [ ] Fristen an prominenter Stelle (Fristenbox oder Fristentabelle am Anfang)
- [ ] Klare Markdown-Gliederung mit Überschriften

## Ergebnis-Format

```markdown
## Strukturprüfung — Ergebnis

| Baustein | Status | Anmerkung |
|---|---|---|
| Verfahrensidentifikation | vollstaendig | — |
| Einleitungssatz | vollstaendig | — |
| Zusammenfassung | unvollstaendig | Nächste Verfahrenshandlung fehlt |
| Sachverhaltschronologie | vollstaendig | — |
| Verfahrenschronologie | vollstaendig | — |
| Parteivortrag-Tabelle | vollstaendig | — |
| Beweismittel-Tabelle | unvollstaendig | B-Anlagen nicht erfasst |
| Rechtsargumente-Tabelle | vollstaendig | — |

**Gesamtergebnis:** ÜBERARBEITUNG ERFORDERLICH
**Offene Punkte:** [Anzahl]
```

## Adressat und Tonfall

Adressat: Sachbearbeiter / Kanzleiintern — Tonfall: sachlich-juristisch, präzise Mängelangabe.
