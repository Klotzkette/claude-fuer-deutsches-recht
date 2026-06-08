---
name: ampel-system
description: "Setzt ein dreistufiges Ampelsystem in der Excel-Arbeitsmappe um: gruen fuer vollstaendig, gelb fuer pruefungsbeduerftig, rot fuer fehlt oder fehlerhaft. Wird per bedingter Formatierung auf allen Reitern angewandt."
---

# Ampelsystem fuer Status

## Rolle und Fokus
Dreistufige Ampel (gruen/gelb/rot) als bedingte Formatierung in der Excel-Arbeitsmappe und als Farbtag in Padlet-Karten. Verdichtet komplexe Statuslagen auf einen Blick.

## Vorgehen

1. **Schwellenwerte definieren** — Was zaehlt als gruen, gelb, rot? Standard: gruen = vollstaendig und unterschrieben und zugestellt; gelb = vorhanden, aber Pruefbedarf; rot = fehlt, Frist ueberschritten oder Wirksamkeit unklar.
2. **Bedingte Formatierung in Excel setzen** — Pro Reiter eine Regel auf die Status-Spalte; Hintergrundfarbe statt Schriftfarbe (lesbar im Druck und PDF-Export).
3. **Fristen-Ampel separat** — Im optionalen Fristen-Reiter Restzeit-Ampel: gruen > 30 Tage, gelb 8-30, rot <= 7.
4. **Mismatch zwischen Reiter 2 und 3 visualisieren** — Wenn Dokument in Reiter 2 als vorhanden markiert, aber Anlage in Reiter 3 fehlend: gelb in Reiter 2.

## Anwendungsbeispiel
LausitzStorage-Akte Stand 02.06.2026: 4 rote Eintraege (Drawstop NordCap, Anlage 4 Konsortialvertrag fehlt, Zugangsnachweis LEAG-Kuendigungsdrohung unklar, Avalstatus 50Hertz unbestaetigt), 7 gelbe (drei Cap-Table-Versionen mit Abweichungen, zwei Unterschriften fragwuerdig, ein Gesellschafterbeschluss inhaltlich unklar, Drawstop-Schreiben unklar zugegangen), Rest gruen.

## Output-Module
- Bedingte-Formatierung-Regeln je Reiter (Hintergrundfarbe auf Status-Spalte)
- Restzeit-Ampel im Fristen-Reiter mit Schwellen 30/8 Tage
- Ampel-Konsistenz-Pruefung zwischen Reiter 2 und 3
