---
name: copy-paste-fehler-erkennung
description: "Erkennt typische Copy-Paste-Situationen: alte Parteinamen, abweichende Vertragsbezeichnungen, falsche Daten in Standardabsaetzen und uebernommene Klauseln aus Vorlaeuferdokumenten. Liefert eine kommentierte Auffaelligkeitsliste."
---

# Copy-Paste-Fehler erkennen

## Rolle und Fokus
Findet uebernommene Textstellen aus Vorlaeuferdokumenten: alte Parteinamen, falsche Datumsangaben in Standardabsaetzen, Verweise auf nicht existente Anhaenge oder Beschlüsse.

## Anwendungsbeispiel
Wandeldarlehen NordCap vom 14.03.2026: § 4 verweist auf 'Gesellschafterbeschluss vom 22.01.2026' — solcher Beschluss existiert nicht; jung uebernommene Klausel aus Wandeldarlehensvorlage einer anderen Portfoliogesellschaft. § 11 nennt 'LausitzWind GmbH' statt 'LausitzStorage 200 GmbH i.G.' an einer Stelle.

## Output-Module
- Auffaelligkeitsliste mit Fundstelle, Verdacht, Verweisziel
- Querliste an Skill `unterschriftspruefung` (Beschluss als Wirksamkeitsbedingung)
- Reparatur-Vorschlag für Nachtragsvereinbarung

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

