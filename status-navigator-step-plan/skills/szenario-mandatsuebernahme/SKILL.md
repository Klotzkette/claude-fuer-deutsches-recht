---
name: szenario-mandatsuebernahme
description: "Anwendungsszenario Uebernahme eines Mandats mit ungeordneter Dokumentenlage. Status-Navigator erzeugt schnell Klarheit ueber Status und naechste Schritte. Markiert Sofortpflichten und uebersehene Fristen."
---

# Szenario Mandatsuebernahme

## Rolle und Fokus
Uebernahme eines Mandats mit ungeordneter Dokumentenlage. Status-Navigator erzeugt schnell Klarheit ueber Status und naechste Schritte. Markiert Sofortpflichten und uebersehene Fristen.

## Vorgehen

1. **Mandatsuebergabe-Notiz lesen** — Aufgaben, offene Fristen, laufende Verfahren, Kommunikationsstaende.
2. **Vorgaengerakte importieren** — Skill `dokumenten-inventur-grob` auf den uebernommenen Bestand.
3. **Fristen-Soforterhebung** — Skill `excel-reiter-fristen-optional` mit Restzeit-Ampel als Erstes ausfuellen.
4. **Offene Sofortpflichten** — Berufsrechtliche Wiedervorlagen, drohende Verjaehrung, anwaltliche Wiedereinsetzungs- und Heilungsoptionen.
5. **Erstkontakt-Plan** — Wer ist heute zu informieren? Mandant, Gegner, Gericht, Behoerde?

## Anwendungsbeispiel
LausitzStorage waere bei hypothetischer Mandatsuebernahme von Pohlmann & Pohlmann an andere Kanzlei: Uebergabenotiz nennt 4 rote Reiter-1-Eintraege und 1 gelbe Frist (Wandlungsfenster 30.09.2026). Sofortmassnahmen: Zugangsnachweis Drawstop sichern, Anlage 4 Konsortial nachfordern, Avalstatus 50Hertz klaeren — alles innerhalb 5 Werktagen.

## Output-Module
- Uebernahme-Reiter mit roten und gelben Eintraegen aus Vorgaengerakte
- Frist-Soforterhebung mit Restzeit-Ampel
- Erstkontaktliste fuer den Tag nach Mandatsuebernahme
