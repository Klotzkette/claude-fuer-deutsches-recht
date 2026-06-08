---
name: fristen-risikoampel-mandantenkommunikation
description: "Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Kanzlei Builder Hub."
---

# Fristen- und Risikoampel

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: BRAO § 51 Mindestversicherung sofort, FAO § 4 Fachanwalt-Antrag 3-Jahres-Frist (10 % Mindestumfang), GwG-Risikoanalyse jährlich, beA Pflichtnutzung seit 01.01.2022.
- Tragende Normen verifizieren: BRAO §§ 5, 7, 14, 27, 43 ff., 49b, 51 (Berufshaftpflicht), BORA, FAO, RVG §§ 1 ff., GwG §§ 2, 10, 11, 43 (Kanzlei als Verpflichteter), DSGVO, beA-Bedingungen, Steuerrecht (EStG, UStG, GewStG) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Kanzleigründer, Kammer, BRAK, Versicherer (Berufshaftpflicht), Mandant, Steuerberater, IT-Dienstleister (beA, RA-MICRO/AnNoText).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Kanzleihandbuch, Datenschutz-Konzept, Geldwäsche-Risikoanalyse, Mandatsvertrag, Honorarvereinbarung, Versicherungspolice, Sozietätsvertrag, beA-Konfiguration — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Risikoampel Builder-Hub
- **Rot:** `validate-yaml-frontmatter.py` oder `validate-plugin-structure.mjs` schlägt fehl -- darf nicht ausgeliefert werden.
- **Rot:** Komma-Zahl in `description` (Frontmatter) -- "1,5" statt "1.5"; Validator schlägt fehl.
- **Rot:** Skill-Description enthält Mandantendaten / Beispiele mit Klarnamen.
- **Rot:** Bezug auf erfundene BGH-/EuGH-Az. im Skill-Inhalt.
- **Gelb:** Skill verweist auf andere Skills, die umbenannt wurden -> broken link.
- **Gelb:** Plugin enthält Skill ohne Querverweise zum Anschluss-Skill.
- **Gelb:** Skill bezieht sich auf Norm-Fassung, ohne Fassungsdatum zu nennen (z. B. "ZPO" ohne Hinweis auf KostRMoG / Beschleunigungsnovelle).
- **Grün:** Validator ohne Fehler, Querverweise konsistent, Halluzinationssperre eingebaut, Sprache Deutsch.

## Update-Fristen
- **Quartalsweise:** Norm-Updates der zentralen Gesetzbücher (BGB, ZPO, StGB, AktG, UStG, EStG, ggf. spezielle Verfahrensordnungen).
- **Monatlich:** Rspr.-Updates für Highlight-Entscheidungen (BGH Pressemitteilungen, BVerfG, EuGH).
- **Ad-hoc:** bei tagesaktuellen Gesetzes-/Verordnungsänderungen (z. B. GPSR, AI Act, eIDAS 2.0).

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

