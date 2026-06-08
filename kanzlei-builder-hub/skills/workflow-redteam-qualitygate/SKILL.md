---
name: workflow-redteam-qualitygate
description: "Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Kanzlei Builder Hub."
---

# Red-Team Qualitygate

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 51 Mindestversicherung sofort, FAO § 4 Fachanwalt-Antrag 3-Jahres-Frist (10 % Mindestumfang), GwG-Risikoanalyse jährlich, beA Pflichtnutzung seit 01.01.2022.
- Tragende Normen verifizieren: BRAO §§ 5, 7, 14, 27, 43 ff., 49b, 51 (Berufshaftpflicht), BORA, FAO, RVG §§ 1 ff., GwG §§ 2, 10, 11, 43 (Kanzlei als Verpflichteter), DSGVO, beA-Bedingungen, Steuerrecht (EStG, UStG, GewStG) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Kanzleigründer, Kammer, BRAK, Versicherer (Berufshaftpflicht), Mandant, Steuerberater, IT-Dienstleister (beA, RA-MICRO/AnNoText).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Kanzleihandbuch, Datenschutz-Konzept, Geldwäsche-Risikoanalyse, Mandatsvertrag, Honorarvereinbarung, Versicherungspolice, Sozietätsvertrag, beA-Konfiguration — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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

## Builder-Hub Quality-Gate für neue Skills
- **Validator-Lauf:** `python3 scripts/validate-yaml-frontmatter.py` und `node scripts/validate-plugin-structure.mjs` — beide ohne Fehler/Warnungen.
- **Frontmatter:** Genau `name` und `description`. Keine weiteren Felder (kein `triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- **Description-Länge:** max. 1024 Zeichen, KEINE Zahlen-Kommas (statt "1,5" schreibe "1.5" oder "eineinhalb").
- **Skill-Name:** max. 64 ASCII-Zeichen, kein Umlaut, kein Sonderzeichen außer Bindestrich.
- **Innenstruktur:** (1) Zweck/Anwendungsfall, (2) Eingaben, (3) Ablauf/Checkliste, (4) Quellenpflicht, (5) Ausgabeformat, (6) Beispiele.
- **Sprache:** Deutsch. Englische Fachbegriffe nur, wenn etabliert und erklärt.
- **Halluzinationssperre:** Keine erfundenen BGH/EuGH-Az.; "BGH ständige Rspr." statt erfundene Az.; Kommentar-/Aufsatz-Fundstellen nur mit Live-Beleg.
- **Reproduzierbarkeit:** Skill muss auch bei Re-Run mit gleichen Eingaben gleiches Ergebnis liefern (Modell-Streuung minimieren durch klare Checklisten).
- **Plugin-Konsistenz:** Skill verweist auf andere Skills des Plugins; keine Selbstreferenz.
- Falle: Beim Refactoring den Skill-Name ändern, ohne Verweise in anderen Skills nachzuziehen → broken-links nicht prüfbar.

