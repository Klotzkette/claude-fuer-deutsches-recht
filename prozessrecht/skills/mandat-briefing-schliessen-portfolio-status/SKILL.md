---
name: mandat-briefing-schliessen-portfolio-status
description: "Mandantenbriefing für Gerichtstermin erstellen: Ablauf, Verhaltenshinweise, Beweisfragen. Normen: §§ 373 ff. ZPO. Prüfraster: Beweislast, Zeugenvorbereitung, Verhandlungsstrategien. Output: Briefingdokument für Mandanten vor Termin. Abgrenzung: nicht Zeugenvorbereitung (eigener Skill) im Prozessrecht."
---

# Mandat-Briefing

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ausgabeformat

```
MANDAT-BRIEFING
──────────────────────────────────────
Mandat: [Slug]
Parteien: [Kläger] ./. [Beklagter]
Gericht / Az.: [Gericht], Az. [JJJJ] [Aktenzeichen]
Verfahrensstufe: [z. B. Berufung – OLG Frankfurt]
Stand: TT.MM.JJJJ
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

<!-- AUDIT 27.05.2026
Halluzinierte Referenz geloescht. Keine Ersatzquelle gefunden.
-->

