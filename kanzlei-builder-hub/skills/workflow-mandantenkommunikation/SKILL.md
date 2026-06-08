---
name: workflow-mandantenkommunikation
description: "Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Kanzlei Builder Hub."
---

# Mandantenkommunikation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 51 Mindestversicherung sofort, FAO § 4 Fachanwalt-Antrag 3-Jahres-Frist (10 % Mindestumfang), GwG-Risikoanalyse jährlich, beA Pflichtnutzung seit 01.01.2022.
- Tragende Normen verifizieren: BRAO §§ 5, 7, 14, 27, 43 ff., 49b, 51 (Berufshaftpflicht), BORA, FAO, RVG §§ 1 ff., GwG §§ 2, 10, 11, 43 (Kanzlei als Verpflichteter), DSGVO, beA-Bedingungen, Steuerrecht (EStG, UStG, GewStG) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Kanzleigründer, Kammer, BRAK, Versicherer (Berufshaftpflicht), Mandant, Steuerberater, IT-Dienstleister (beA, RA-MICRO/AnNoText).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Kanzleihandbuch, Datenschutz-Konzept, Geldwäsche-Risikoanalyse, Mandatsvertrag, Honorarvereinbarung, Versicherungspolice, Sozietätsvertrag, beA-Konfiguration — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Kommunikations-Struktur
- **Was wurde gebaut:** Plugin-Name, Skill-Name(n), Version (semantisch).
- **Validator-Status:** `validate-yaml-frontmatter.py` und `validate-plugin-structure.mjs` -- OK / Fehler.
- **Was ist NICHT enthalten:** Skill-Grenzen klar benennen (kein Live-Quellencheck, kein Mandantengeheimnis-Hosting, kein KI-Output ohne Verifizierung).
- **Nächste Schritte:** Testlauf vorgesehen, Rollout-Termin, Schulungsbedarf.
- **Risiken / offene Punkte:** Halluzinationsrisiken, Mandantenakte-Konformität, BORA-Pflichten der Kanzlei beim Einsatz.

## Adressatengerecht
- **Kanzleipartner:** Geschäftsnutzen, Risikohinweise, Lizenz/Datenschutz, Schulungsaufwand.
- **IT/Admin:** Installations-/Update-Pfad, Validator-Pipeline, Abhängigkeiten.
- **Wissensmanagement:** Pflege, Zitationsstandard, Update-Zyklus für Rechtsprechungs- und Norm-Änderungen.

## Anti-Muster
- Versprechen "rechtssichere KI" -- KI ist nie ohne Verifizierung rechtssicher (Verschwiegenheit § 43a Abs. 2 BRAO, § 203 StGB, Halluzinationsrisiken).
- "Wir ersetzen den Anwalt" -- Skill ist Werkzeug, kein Mandatsverhältnis.

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

