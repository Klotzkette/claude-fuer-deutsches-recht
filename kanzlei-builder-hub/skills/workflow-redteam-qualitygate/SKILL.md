---
name: workflow-redteam-qualitygate
description: "Für Red-Team Qualitygate: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. Fachgebiet: Kanzlei-Builder-Hub."
---

# Red-Team Qualitygate

## Arbeitsauftrag

Dieser Arbeitsgang macht **Red-Team Qualitygate** im Bereich **kanzlei-builder-hub** sofort bearbeitbar: erst Akte lesen, dann Rollen, Ziel, Fristen, Belege und Entscheidungspunkte ordnen. Rückfragen kommen nur, wenn sie die rechtliche Weiche, den richtigen Adressaten oder das Arbeitsprodukt wirklich verändern.

## Aktenstart ohne Leerlauf

1. Vorhandene Dokumente, Dateinamen, Metadaten, Anlagen und erkennbare Fristen auswerten, bevor Fragen gestellt werden.
2. Sichere Tatsachen, plausible Annahmen, streitige Behauptungen und fehlende Belege in vier getrennten Spalten erfassen.
3. Parteirolle, Gegner/Behörde/Gericht, Zuständigkeit, Verfahrensstand und gewünschtes Ergebnis knapp bestimmen.
4. Sofortige Risiken markieren: Notfrist, Zustellung/Zugang, Verjährung, Sanktion, Vollstreckung, Register-/Portalfrist, Beweisverlust.
5. Danach nur noch die fehlenden Punkte fragen, die den nächsten Schritt ändern.

## Fachliche Anker

- BRAO §§ 43, 43a, 43e, 46 ff.; BORA §§ 2, 3, 6, 11, 12; RVG/VV RVG bei Kosten- und Vergütungsfragen.
- ZPO § 130d und beA-Pflichten; DSGVO Art. 5, 6, 28, 32; GeschGehG §§ 2, 4 bei vertraulichen Mandatsinformationen.
- Bei Kommunikation immer Mandatsgeheimnis, Interessenkollision, Sachlichkeitsgebot, Fristwahrung und Dokumentationsspur prüfen.

## Arbeitsprodukt

- **Kurzdiagnose:** Was ist wahrscheinlich los, welche Rechtsfrage trägt den Fall, was ist sofort zu tun?
- **Belegmatrix:** Tatsache, Quelle, Fundstelle/Anlage, Beweiswert, Lücke, Nachforderung.
- **Risikoampel:** Grün/gelb/rot mit knapper Begründung und nächstem sicheren Schritt.
- **Entwurf:** je nach Fall E-Mail, Mandantenmemo, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Fristenplan.
- **Fehlerbremse:** keine erfundenen Normen, keine Blindzitate, keine Tatsachenergänzung ohne Aktenbeleg.

## Ergänzende Hinweise

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
