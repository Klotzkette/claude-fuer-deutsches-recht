---
name: aktenauszug-strukturpruefung
description: "Fertig erstellten Aktenauszug auf Vollständigkeit prüfen: alle Bausteine vorhanden Fristen hervorgehoben neutrale Sprache. Normen §§ 128-134 253 ZPO. Prüfraster Bausteine-Vollständigkeit Fristen-Markierung Neutralitaets-Check Sprach-Qualitaet. Output Prüfergebnis-Bericht Lueckenliste Verbesserungshinweise. Abgrenzung zu aktenauszug-erstellen (Erstellung) und neutralitaetsprüfung (Wertungs-Check)."
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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
