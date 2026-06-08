---
name: szenario-finanzierungsstruktur-bereinigen
description: "Anwendungsszenario komplexe Finanzierungsstruktur bereinigen. Status-Navigator erfasst Wandeldarlehen, Bankfinanzierung, Gesellschafterdarlehen, sonstige Einlagen und Stundungen. Stellt Konditionen und Rangfolge zusammen und vergleicht Cap Tables mit Vertraegen."
---

# Szenario Finanzierungsstruktur bereinigen

## Rolle und Fokus
Komplexe Finanzierungsstruktur bereinigen. Status-Navigator erfasst Wandeldarlehen, Bankfinanzierung, Gesellschafterdarlehen, sonstige Einlagen und Stundungen.

## Vorgehen

1. **Instrumentenkarte** — Skill `erweiterung-rangfolge-reiter` als Ausgangspunkt.
2. **Konditionsabgleich** — Zinssatz, Faelligkeit, Tilgungsplan, Sicherheiten pro Instrument; Stillstand- und Subordinationsvertraege beachten.
3. **Wandlungsereignisse und Optionsfristen** — Wandlung in Anteile, Optionsausuebung, Rangrueckungsoptionen.
4. **Konsistenz Cap-Table vs. Finanzierungsstruktur** — Wandelinstrumente sind in Cap Table erst nach Wandlung sichtbar; Pre-Money/Post-Money klar trennen.
5. **Step-Plan-Folge im Workflow-Reiter** — Wer macht was bis wann (Verzicht, Stundung, Anpassungsnachtrag, neue Beschluesse)?

## Anwendungsbeispiel
LausitzStorage Bereinigung: Senior-Darlehen NordCap 80 Mio EUR, Wandeldarlehen NordCap 22 Mio EUR (Reparaturvereinbarung vom 04.06.2026 verlaengert Wandlungsfenster), Konsortial Stadtwerke Cottbus 25 Mio EUR (Sicherungsabtretung Stromabnahmevertrag), Avalrahmen ILB 8 Mio EUR (LEAG-Pachtsicherung), Gesellschafterstundung Bauernfeind 1,2 Mio EUR. Vier Klaerpunkte im Workflow.

## Output-Module
- Instrumentenkarte mit Rang und Sicherheit
- Konditionsuebersicht je Instrument
- Step-Plan mit Bereinigungs-Massnahmen und Verantwortlichkeit
