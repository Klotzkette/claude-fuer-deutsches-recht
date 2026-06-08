---
name: excel-reiter-fristen-optional
description: "Fuegt optional einen Reiter Fristen hinzu: Kuendigungsfristen, Wandlungsfristen, Verjaehrungsfristen, Ablaufdaten und Hemmungstatbestaende. Beruht ausschliesslich auf Mandatsangaben und Vertragstext — keine eigene rechtliche Bewertung."
---

# Optionaler Reiter Fristen

## Rolle und Fokus
Optionaler Reiter Fristen. Kuendigungsfristen, Wandlungsfristen, Verjaehrungsfristen, Ablaufdaten, Hemmungstatbestaende. Beruht auf Mandatsangaben und Vertragstext.

## Vorgehen

1. **Pro Frist eine Zeile** — Bezeichnung, Vertragsklausel, Beginn, Lauf, Ende, Verlaengerung, Hemmungstatbestand.
2. **Drei Frist-Klassen** — materiell (Wandlung, Optionsausuebung), prozessual (Klage, Widerspruch), berufsrechtlich/intern (Wiedervorlage).
3. **Restzeit-Ampel** — gruen > 30 Tage, gelb 8-30, rot <= 7 (bedingte Formatierung).
4. **Sofortmassnahmen-Spalte** — Was muss bei Erreichen der gelben/roten Stufe geschehen?
5. **Querverweis Frist-Erfuellung** — Welches Dokument muss bis Frist erstellt/zugestellt sein? Verweis in Reiter 3/4.

## Anwendungsbeispiel
LausitzStorage Fristen-Reiter: Wandlungsfenster Wandeldarlehen NordCap laeuft 01.07.2026 ab (rot, da 24 Tage Restzeit zum Mandatsbeginn 02.06.2026 — Reparaturvereinbarung verlaengert auf 30.09.2026). LEAG-Heilungsfrist Beibringungspflicht laeuft 30.06.2026 ab (gelb). BImSchG-Klage gegen Vorbescheid haette 06.06.2026 Anfangsmoment — eilbeduerftig.

## Output-Module
- Fristen-Reiter mit Restzeit-Ampel und Sofortmassnahmen-Spalte
- Wiedervorlage-Eintraege fuer das Anwalts-DMS
- Querverweis in Reiter 4 (Workflow): welche Schritte sind bis welcher Frist zu erledigen
