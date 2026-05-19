---
name: kaltstart-interview
description: "Einrichtungs-Interview für das Prozessrecht-Plugin – erfasst Kanzleiart, Rolle, Praxisschwerpunkte, Risikobereitschaft, Mandatslandschaft und Kanzleistil und schreibt die CLAUDE.md. Verwenden bei der Ersteinrichtung, wenn der Nutzer das Praxisprofil neu erstellen oder die Integrations-Verfügbarkeit prüfen möchte."
---

# Kaltstart-Interview

## Zweck

Einmaliges Einrichtungsinterview für das Prozessrecht-Plugin. Erfasst das Praxisprofil der Kanzlei oder Rechtsabteilung und schreibt die Konfiguration in CLAUDE.md. Jeder nachfolgende Skill liest aus dieser Datei den Kontext – ohne Kaltstart arbeiten die Skills mit unvollständigen Voreinstellungen.

## Eingaben

Keine Voreingaben erforderlich. Das Interview fragt alle benötigten Felder interaktiv ab. Flags:
- `--redo`: Bestehendes Profil überschreiben
- `--check-integrations`: Nur Integrations-Verfügbarkeit prüfen, Profil nicht ändern

## Ablauf

### Schritt 1: Kanzlei- und Rollentyp

Fragen:
- „In welcher Rolle verwenden Sie das Plugin?" → Optionen: (a) Rechtsanwalt / Sozietät, (b) Syndikusrechtsanwalt / Rechtsabteilung, (c) Referendar / Berufseinsteiger, (d) Richter / wissenschaftlicher Mitarbeiter
- „Wie viele aktive Mandate bearbeiten Sie typischerweise gleichzeitig?"
- „Arbeiten Sie mit externen Korrespondenzanwälten oder außenstehenden Kanzleien?"

### Schritt 2: Praxisschwerpunkte

Mehrfachauswahl:
- Zivilrecht allgemein (ZPO)
- Handels- und Gesellschaftsrecht
- Bau- und Architektenrecht (§§ 631 ff. BGB, VOB/B)
- Arbeitsrecht (ArbGG)
- Familien- und Erbrecht (FamFG)
- Verwaltungsrecht (VwGO)
- Steuerrecht (FGO)
- Strafrecht / Strafverteidigung (StPO)
- Marken-/Patent-/Urheberrecht
- Wettbewerbsrecht (UWG)
- Insolvenzrecht (InsO)
- Mietrecht

### Schritt 3: Risikobereitschaft und Strategie

- „Wie würden Sie Ihre Risikostrategie beschreiben?" → (a) konservativ (Prozesse vermeiden, Vergleiche bevorzugen), (b) ausgewogen, (c) aggressiv (Ansprüche vollständig verfolgen)
- „Führen Sie überwiegend als Kläger oder Beklagter?" → (a) Kläger, (b) Beklagter, (c) beide gleich häufig
- „Was ist Ihr primäres Gericht?" (freitextlich, z. B. „LG Frankfurt a. M.", „ArbG München")

### Schritt 4: Kanzleistil

- „Bevorzugen Sie Gutachtenstil oder Urteilsstil in internen Memos?" → (a) immer Gutachtenstil, (b) intern Gutachten, extern Urteils, (c) situationsabhängig
- „Haben Sie besondere Formatierungsvorgaben?" (z. B. Seitennummerierung, Randnummern, Briefkopf-Muster)
- „Bevorzugen Sie Rangnummern in Schriftsätzen?"

### Schritt 5: Vergütung und Kosten

- „Wie rechnen Sie überwiegend ab?" → (a) gesetzliche Gebühren nach RVG, (b) Stunden- / Zeithonorar (§ 3a RVG), (c) Pauschalhonorar, (d) Erfolgshonorar (§ 4a RVG)
- „Benötigen Sie automatische Streitwert- und Kostenberechnungen?"

### Schritt 6: Integrations-Check

Das Plugin prüft:
- **Outlook MCP** – für automatische Gegenseite-Status-E-Mails
- **Kalender MCP** – für automatische Fristenerinnerungen
- **GitHub MCP** – für Versions­control der Mandatsdaten

Ausgabe: „[Integration] – verfügbar / nicht verfügbar. Fallback: [Markdown-Datei]."

### Schritt 7: CLAUDE.md schreiben

Das Plugin schreibt alle erfassten Werte in die YAML-Felder von CLAUDE.md (Abschnitt 6). Anschließend: Bestätigung und Zusammenfassung.

## Quellen und Zitierweise

- BRAO, insbesondere §§ 43, 43a, 49b (Vergütung, Verschwiegenheit, Sachlichkeitsgebot).
- BORA §§ 2, 3 (Grundpflichten, Sachlichkeit).
- RVG §§ 1–3a (Anwendungsbereich, Vergütungsvereinbarung).
- Henssler/Prütting, BRAO, 5. Aufl. 2019, § 43a Rn. 45 ff. (Verschwiegenheitspflicht).

## Ausgabeformat

1. **Interaktiver Dialog** (sequenzielle Fragen)
2. **Zusammenfassung** am Ende: Tabellarische Übersicht aller erfassten Werte
3. **CLAUDE.md-Update:** Automatisch, sofern bestätigt
4. **Bestätigungs-Anzeige:** „Praxisprofil gespeichert. Sie können jetzt alle Skills verwenden."

## Risiken / typische Fehler

- **Unvollständiges Profil:** Wenn Felder leergelassen werden, arbeiten Skills mit Standardwerten – diese sind nicht kanzleispezifisch. Nach Einrichtung mit `/anpassen` korrigieren.
- **Rollenwahl falsch:** Syndikusrechtsanwalt hat andere Schweigepflichtgrenzen und Vertretungsverbote (§ 46c BRAO) als freier Anwalt – Rollenwahl im Profil ist berufsrechtlich relevant.
- **Vergütungsvereinbarung:** Stundenhonorar erfordert Textform (§ 3a Abs. 1 RVG); das Plugin dokumentiert die Wahl, ersetzt aber keine rechtsgültige Mandatsvereinbarung.
- **Integrations-Fehlkonfiguration:** Outlook/Kalender MCP ohne korrekte Authentifizierung führt zu fehlgeschlagenen Aktionen; immer `--check-integrations` nach Konfigurations­änderung ausführen.
